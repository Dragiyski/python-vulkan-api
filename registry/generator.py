import ctypes
import ast
import re
from collections import OrderedDict
from pathlib import Path
from .context import Context
from .platform import CPlainType, CPointerType, CArrayType, CComplexType, CFunctionType
from os import linesep

enum_class_suffix = {
    'enum': 'Enum',
    'bitmask': 'Flag',
    None: ''
}

enum_base_class = {
    'enum': 'IntEnum',
    'bitmask': 'IntFlag',
    None: 'int'
}

ctypes_types = [name for name in dir(ctypes) if name.startswith('c_')]


class GeneratorError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(**kwargs)


class Generator:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir).resolve()

    def _generate_base_source(self, context: Context):
        code = ['import ctypes', 'from enum import IntEnum, IntFlag', '']
        exports = []
        for enum_class in ['enum', 'bitmask']:
            plain_type_map = {k.__name__: v for k, v in context.plain_ctype_class[enum_class].items()}
            for ctype_name in sorted(plain_type_map.keys()):
                descriptor = plain_type_map[ctype_name]
                exports.append(descriptor['class_name'])
                code.extend(
                    [
                        'class %s(%s):' % (descriptor['class_name'], descriptor['base_class_name']),
                        '    def __init__(self, *args, **kwargs):',
                        '        self._as_parameter_ = ctypes.%s(%s(self))' % (ctype_name, descriptor['python_type']),
                        '', ''
                    ]
                )
            code.append('Vulkan%s = {' % enum_class_suffix[enum_class])
            for ctype_name in sorted(plain_type_map.keys()):
                descriptor = plain_type_map[ctype_name]
                code.append('    ctypes.%s: %s,' % (ctype_name, descriptor['class_name']))
            code.extend(['}', ''])
        plain_type_map = {k.__name__: v for k, v in context.plain_ctype_class['value'].items()}
        for ctype_name in sorted(plain_type_map.keys()):
            descriptor = plain_type_map[ctype_name]
            exports.append(descriptor['class_name'])
            code.extend(
                [
                    'class %s(%s):' % (descriptor['class_name'], descriptor['python_type']),
                    '    def __new__(cls, *args, **kwargs):',
                    '        value = super().__new__(cls, *args, **kwargs)',
                    '        value._as_parameter_ = ctypes.%s(%s(value))' % (ctype_name, descriptor['python_type']),
                    '        return value',
                    '', ''
                ]
            )
        code.append('VulkanValue = {')
        for ctype_name in sorted(plain_type_map.keys()):
            descriptor = plain_type_map[ctype_name]
            code.append('    ctypes.%s: %s,' % (ctype_name, descriptor['class_name']))
        code.extend(['}', ''])

        code.extend(
            [
                "if hasattr(ctypes, 'WINFUNCTYPE'):",
                '    VKAPI_CALL = ctypes.WINFUNCTYPE',
                '    VKAPI_PTR = ctypes.WINFUNCTYPE',
                'else:',
                '    VKAPI_CALL = ctypes.CFUNCTYPE',
                '    VKAPI_PTR = ctypes.CFUNCTYPE',
                ''
            ]
        )
        exports.extend(['VKAPI_CALL', 'VKAPI_PTR'])
        code.append('__all__ = [')
        for name in sorted(exports):
            code.append('    %r,' % name)
        code.extend([']', ''])
        return linesep.join(code)

    def _generate_enum_source(self, context: Context, enum_name: str):
        if enum_name not in context.enum_map:
            raise GeneratorError('No enum named "%s" found.' % enum_name, name = enum_name)
        descriptor = context.enum_map[enum_name]
        type_descriptor = context.plain_ctype_class[descriptor['class']][descriptor['ctype'].ctype()]
        code = ['from enum import %s' % type_descriptor['base_class_name'], '']
        code.append('class %s(%s):' % (enum_name, type_descriptor['base_class_name']))
        values = {}
        for value_name in descriptor['values']:
            value_descriptor = context.value_map[value_name]
            values[value_name] = '    %s = %r' % (value_name, value_descriptor['value'])
        if len(values) > 0:
            for value_name in sorted(values.keys()):
                code.append(values[value_name])
            alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in values}
            for name in sorted(alias.keys()):
                value = alias[name]
                code.append('    %s = %s' % (name, value))
        else:
            code.append('    pass')
        code.append('')

        return linesep.join(code)

    def _generate_value_source(self, context: Context):
        code = ['import ctypes']
        enum_set = set()
        exports = set()
        for descriptor in context.value_map.values():
            if 'enum_name' in descriptor:
                enum_set.add(descriptor['enum_name'])
        for enum_name in sorted(enum_set):
            code.append('from ._vulkan_enum.%s import %s' % (enum_name, enum_name))
        code.append('')
        value_map = {}
        for name, descriptor in context.value_map.items():
            exports.add(name)
            if 'enum_name' in descriptor:
                value_map[name] = '%s = %s.%s' % (name, descriptor['enum_name'], name)
            else:
                value_map[name] = '%s = %r' % (name, descriptor['value'])
        for name in sorted(value_map.keys()):
            code.append(value_map[name])
        code.append('')
        for name in sorted(context.object_macro_map.keys()):
            exports.add(name)
            descriptor = context.object_macro_map[name]
            code.append('%s = %r' % (name, descriptor['value']))
        code.append('')
        for name in sorted([k for k, v in context.func_macro_map.items() if 'python_node' in v]):
            exports.add(name)
            descriptor = context.func_macro_map[name]
            func_code = ast.unparse(descriptor['python_node']).split(linesep)
            func_code.append('')
            code.extend(func_code)
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in context.value_map}
        for name in sorted(alias.keys()):
            exports.add(name)
            code.append('%s = %s' % (name, alias[name]))
        code.append('__all__ = [')
        for name in sorted(exports):
            code.append('    %r,' % name)
        code.extend([']', ''])
        return linesep.join(code)

    def _generate_complex_source(self, context: Context, name: str):
        code = ['import ctypes', '']
        ctype = context.ctypes_map[name]
        ctype: CComplexType
        struct_desc = context.struct_map[name]

        def generate_class_body():
            code.append('    _init_ = []')
            for usage_name in ['extends', 'extended_by', 'includes', 'included_in', 'input_of', 'output_of']:
                if len(struct_desc[usage_name]) > 0:
                    code.append('    _%s_ = {' % usage_name)
                    for reference in sorted(struct_desc[usage_name]):
                        code.append('        %r,' % reference)
                    code.append('    }')
                else:
                    code.append('    _%s_ = set()' % usage_name)
            code.append('    _python_name_ = {')
            for member_name in struct_desc['ctype'].member_list:
                python_name = struct_desc['ctype'].member_map[member_name]['python_name']
                if len(python_name) > 1:
                    python_name = [word for word in python_name if re.fullmatch(r'([ps])\1*', word) is None]
                python_name = '_'.join(python_name)
                code.append('        %r: %r,' % (member_name, python_name))
            code.append('    }')
            features = []
            for feature in context.feature_map.values():
                if name in feature['types'] and 'version' in feature:
                    features.append(tuple(feature['version']))
            if len(features) > 0:
                code.append('    _vk_versions_ = {')
                for feature in sorted(features):
                    code.append('        %r,' % (feature,))
                code.append('    }')
            else:
                code.append('    _vk_versions_ = set()')
            extensions = []
            for extension_name, extension_desc in context.ext_map.items():
                if name in extension_desc['types']:
                    extensions.append(extension_name)
            if len(extensions) > 0:
                code.append('    _vk_extensions_ = {')
                for extension in sorted(extensions):
                    code.append('        %r,' % (extension,))
                code.append('    }')
            else:
                code.append('    _vk_extensions_ = set()')
            enum_map = {k: v['type'] for k, v in struct_desc['ctype'].member_map.items() if v['is_enum']}
            if len(enum_map) > 0:
                code.append('    _vk_enum_ = {')
                for k, v in enum_map.items():
                    code.append('        %r: %r,' % (k, v))
                code.append('    }')
            else:
                code.append('    _vk_enum_ = dict()')
            if 'sType' in struct_desc['ctype'].member_map and struct_desc['ctype'].member_map['sType'].get('type', None) == 'VkStructureType' and struct_desc['ctype'].member_map['sType'].get('value', '').startswith('VK_STRUCTURE_TYPE_'):
                code.append('    _vk_structure_type_ = %r' % struct_desc['ctype'].member_map['sType']['value'])
            code.append('')
            code.append('    def __init__(self, *args, **kwargs):')
            code.append('        super().__init__()')
            if 'sType' in struct_desc['ctype'].member_map and struct_desc['ctype'].member_map['sType'].get('type', None) == 'VkStructureType' and struct_desc['ctype'].member_map['sType'].get('value', '').startswith('VK_STRUCTURE_TYPE_'):
                code.append('        from .._vulkan_enum.%s import %s' % ('VkStructureType', 'VkStructureType'))
                code.append('        self.sType = VkStructureType.%s' % struct_desc['ctype'].member_map['sType']['value'])
            code.append('        for function in self._init_:')
            code.append('            function(self, *args, **kwargs)')
            code.append('')
            pass

        code.append('class %s(ctypes.%s):' % (name, ctype.constructor))
        member_types = [ctype.member_map[x]['node'].get('type').get_text() for x in ctype.member_list]
        complex_member_types = set([x for x in member_types if x in context.type_node_map['complex']])
        funcpointer_member_types = set([x for x in member_types if x in context.type_node_map['funcpointer']])
        delay_fields = ctype['delay_fields'] or name in complex_member_types
        in_class_body = True
        if delay_fields or len(complex_member_types) > 0 or len(funcpointer_member_types) > 0:
            generate_class_body()
            in_class_body = False
            code.append('')
            for dependency in sorted([context.ctypes_map[t].name for t in funcpointer_member_types]):
                code.append('from .._vulkan_callback.%s import %s' % (dependency, dependency))
            for dependency in sorted(complex_member_types):
                if dependency != name:
                    code.append('from .%s import %s' % (dependency, dependency))
            code.append('')
            code.append('%s._fields_ = [' % name)
            indent = 1
        else:
            code.append('    _fields_ = [')
            indent = 2
        for member_name in ctype.member_list:
            member_desc = ctype.member_map[member_name]
            if 'bitsize' in member_desc:
                code.append('%s(%r, %s, %d),' % ('    ' * indent, member_name, member_desc['ctype'].to_source(), member_desc['bitsize']))
            else:
                code.append('%s(%r, %s),' % ('    ' * indent, member_name, member_desc['ctype'].to_source()))
        code.append('    ' * (indent - 1) + ']')
        code.append('')
        if in_class_body:
            generate_class_body()
        code.append('%s._type_ = {' % name)
        for member_name in ctype.member_list:
            member_desc = ctype.member_map[member_name]
            code.append('    %r: %s,' % (member_name, member_desc['ctype'].to_source()))
        code.append('}')
        code.append('')
        return linesep.join(code)

    def _generate_command_source2(self, context: Context):
        dep_map = {}
        code = ['import ctypes', 'from .vulkan_base import VKAPI_PTR, VKAPI_CALL']
        fn_code_map = {}
        fn_list = []

        def check_type_dep(ctype):
            if isinstance(ctype, CPointerType):
                check_type_dep(ctype.deref())
            elif isinstance(ctype, CArrayType):
                check_type_dep(ctype.item_ctype)
            elif isinstance(ctype, CComplexType):
                if 'struct' not in dep_map:
                    dep_map['struct'] = set()
                dep_map['struct'].add(ctype.name)
            elif isinstance(ctype, CFunctionType):
                if 'callback' not in dep_map:
                    dep_map['callback'] = set()
                dep_map['callback'].add(ctype.name)

        for type_name in sorted(context.command_node_map.keys()):
            fn_type = context.ctypes_map[type_name]
            check_type_dep(fn_type.return_type)
            for arg in fn_type.argument_types:
                check_type_dep(arg)
            fn_code_map[fn_type.name] = '%s = %s(%s)' % (
                fn_type.name,
                fn_type.constructor,
                ', '.join([fn_type.return_type.to_source()] + [arg.to_source() for arg in fn_type.argument_types])
            )
            fn_list.append(fn_type.name)
        if 'struct' in dep_map and len(dep_map['struct']) > 0:
            for dep_name in sorted(dep_map['struct']):
                code.append('from ._vulkan_type.%s import CType as %s' % (dep_name, dep_name))
        if 'callback' in dep_map and len(dep_map['callback']) > 0:
            code.append('from .vulkan_callback import (')
            for dep_name in sorted(dep_map['callback']):
                code.append('    %s,' % dep_name)
            code.append(')')
        code.append('')
        for fn_name in fn_list:
            code.append(fn_code_map[fn_name])
        code.append('')
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in context.command_node_map}
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        code.append('__all__ = [')
        for fn_name in sorted(fn_list + list(alias.keys())):
            code.append('    %r,' % fn_name)
        code.extend([']', ''])
        return linesep.join(code)
    
    def _generate_callback_descriptor_source(self, context: Context, callback_name: str):
        ctype = context.ctypes_map[callback_name]
        assert isinstance(ctype, CFunctionType)
        info = context.callback_map['PFN_%s' % callback_name]
        code = ['from ..._ctypes import *', '']
        code.append("category = 'callback'")
        code.append('_name_ = %r' % callback_name)
        code.append('_constructor_ = %r' % ctype.constructor)
        code.append('_argument_list_ = %r' % info['arg_list'])
        code.append('_argument_info_ = {')
        for arg_name in info['arg_list']:
            arg_type = info['arg_map'][arg_name]
            code.append('    %r: {' % (arg_name))
            code.append('        %r: %s,' % ('type', arg_type.get_runtime_source()))
            code.append('    },')
        code.append('}')
        code.append('_return_type_ = %s' % info['return'].get_runtime_source())
        code.append('')
        return linesep.join(code)
    
    def _generate_procedure_descriptor_source(self, context: Context, function_name: str):
        ctype = context.ctypes_map[function_name]
        assert isinstance(ctype, CFunctionType)
        info = context.command_map[function_name]
        code = ['from ..._ctypes import *', '']
        code.append("_category_ = 'procedure'")
        code.append('_name_ = %r' % function_name)
        code.append('_constructor_ = %r' % ctype.constructor)
        code.append('_argument_list_ = %r' % info['argument_list'])
        code.append('_argument_info_ = {')
        for arg_name in info['argument_list']:
            arg_desc = info['argument_map'][arg_name]
            code.append('    %r: {' % (arg_name))
            code.append('        %r: %s,' % ('type', arg_desc['ctype'].get_runtime_source()))
            if 'is_string' in arg_desc:
                code.append('        %r: %r,' % ('is_string', arg_desc['is_string']))
            if 'length' in arg_desc:
                code.append('        %r: %r,' % ('length', arg_desc['length']))
            if 'output' in arg_desc:
                code.append('        %r: %r,' % ('output', arg_desc['output']))
            # Special property to signify the length must be handled manually.
            # The value is ignored by the code, and considered a documentation string. 
            if 'length_need_processor' in arg_desc:
                code.append('        %r: %r,' % ('alt_length', arg_desc['length_need_processor'] if arg_desc['length_need_processor'] is not None else ''))
            code.append('    },')
        code.append('}')
        code.append('_return_type_ = %s' % ctype.return_type.get_runtime_source())
        if 'success_code_list' in info:
            code.append('_success_code_list_ = %r' % set(info['success_code_list']))
        if 'error_code_list' in info:
             code.append('_error_code_list_ = %r' % set(info['error_code_list']))
        code.append('')
        return linesep.join(code)

    def _generate_complex_descriptor_source(self, context: Context, type_name: str):
        ctype = context.ctypes_map[type_name]
        assert isinstance(ctype, CComplexType)
        info = context.struct_map[type_name]
        code = ['from ..._ctypes import *', '']
        code.append('_category_ = %r' % (ctype.constructor.lower()))
        code.append('_name_ = %r' % type_name)
        code.append('_member_list_ = %r' % (ctype.member_list))
        code.append('_member_info_ = {')
        for member_name in ctype.member_list:
            member_info = ctype.member_map[member_name]
            code.append('    %r: {' % member_name)
            code.append('        %r: %s,' % ('type', member_info['ctype'].get_runtime_source()))
            if 'type' in member_info:
                member_type = member_info['type']
                code.append('        %r: %r,' % ('type_name', member_type))
                if member_type in context.enum_map:
                    code.append('        %r: %r,' % ('enum', member_type))
                elif member_type in context.struct_map:
                    code.append('        %r: %r,' % (context.ctypes_map[member_type].constructor.lower(), member_type))
            if isinstance(member_info['ctype'], CFunctionType) and ('PFN_%s' % member_info['ctype'].name) in context.type_node_map['funcpointer']:
                code.append('        %r: %r,' % ('callback', member_info['ctype'].name))
            if 'bitsize' in member_info:
                code.append('        %r: %d,' % ('bitsize', member_info['bitsize']))
            if 'length' in member_info:
                code.append('        %r: %r,' % ('length', member_info['length']))
            if 'value' in member_info:
                code.append('        %r: %r,' % ('value', member_info['value']))
            if 'values' in member_info:
                code.append('        %r: %r,' % ('values', member_info['values']))
            if 'is_string' in member_info:
                code.append('        %r: %r,' % ('is_string', member_info['is_string']))
            code.append('    },')
        code.append('}')
        for usage_name in ['extends', 'extended_by', 'includes', 'included_in', 'input_of', 'output_of']:
            if len(info[usage_name]) > 0:
                code.append('_%s_ = {' % usage_name)
                for reference in sorted(info[usage_name]):
                    code.append('    %r,' % reference)
                code.append('}')
            else:
                code.append('_%s_ = set()' % usage_name)
        code.append('')
        return linesep.join(code)

    def _generate_function_source(self, context: Context, name: str):
        ctype = context.ctypes_map[name]
        assert isinstance(ctype, CFunctionType)
        code = ['import ctypes', 'from ..vulkan_base import %s' % (ctype.constructor), '']

        def check_type_dep(ctype):
            nonlocal code
            if isinstance(ctype, CPointerType):
                check_type_dep(ctype.deref())
            elif isinstance(ctype, CArrayType):
                check_type_dep(ctype.item_ctype)
            elif isinstance(ctype, CComplexType):
                code.append('from .._vulkan_type.%s import %s' % (ctype.name, ctype.name))
            elif isinstance(ctype, CFunctionType):
                code.append('from .%s import %s' % (ctype.name, ctype.name))

        check_type_dep(ctype.return_type)
        for arg in ctype.argument_types:
            check_type_dep(arg)
        code.append('')
        code.append(
            '%s = %s(%s)' % (
                ctype.name,
                ctype.constructor,
                ', '.join([ctype.return_type.to_source()] + [arg.to_source() for arg in ctype.argument_types])
            )
        )
        code.append('')
        return linesep.join(code)

    def _generate_callback_init_source(self, context: Context):
        code = []
        for name in sorted(context.ctypes_map[k].name for k in context.type_node_map['funcpointer'].keys()):
            code.append('from ._vulkan_callback.%s import %s' % (name, name))
        code.append('')
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if
            value in context.type_node_map['funcpointer']}
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)

    def _generate_procedure_source(self, context: Context, name: str):
        ctype = context.ctypes_map[name]
        assert isinstance(ctype, CFunctionType)
        code = ['import ctypes', 'from ..vulkan_base import %s' % (ctype.constructor), '']

        def check_type_dep(ctype):
            nonlocal code
            if isinstance(ctype, CPointerType):
                check_type_dep(ctype.deref())
            elif isinstance(ctype, CArrayType):
                check_type_dep(ctype.item_ctype)
            elif isinstance(ctype, CComplexType):
                code.append('from .._vulkan_type.%s import %s' % (ctype.name, ctype.name))
            elif isinstance(ctype, CFunctionType):
                code.append('from .._vulkan_callback.%s import %s' % (ctype.name, ctype.name))

        check_type_dep(ctype.return_type)
        for arg in ctype.argument_types:
            check_type_dep(arg)
        code.append('')
        code.append(
            '%s = %s(%s)' % (
                ctype.name,
                ctype.constructor,
                ', '.join([ctype.return_type.to_source()] + [arg.to_source() for arg in ctype.argument_types])
            )
        )
        code.append('')
        return linesep.join(code)

    def _generate_funcpointer_source(self, context: Context):
        code = ['import ctypes', 'from .vulkan_base import VKAPI_PTR, VKAPI_CALL']
        done = set()
        doing = set()
        postponed = OrderedDict()

        def write_function(name):
            nonlocal code
            if name in done:
                return
            if name in doing:
                raise ReferenceError('Circular reference while resolving callback: %s' % name)
            doing.add(name)
            fn_type = context.ctypes_map[name]
            fn_type: CFunctionType
            check_type_dep(name, fn_type.return_type)
            for arg in fn_type.argument_types:
                check_type_dep(name, arg)
            if name in postponed:
                lines = postponed[name]
            else:
                lines = code
            lines.append(
                '%s = %s(%s)' % (
                    fn_type.name,
                    fn_type.constructor,
                    ', '.join([fn_type.return_type.to_source()] + [arg.to_source() for arg in fn_type.argument_types])
                )
            )
            done.add(name)
            doing.remove(name)

        fn_code_map = {}
        fn_list = []

        def check_type_dep(name, ctype):
            if isinstance(ctype, CPointerType):
                check_type_dep(name, ctype.deref())
            elif isinstance(ctype, CArrayType):
                check_type_dep(name, ctype.item_ctype)
            elif isinstance(ctype, CComplexType):
                postponed.setdefault(name, [])
                postponed[name].append('from .vulkan_type.%s import %s' % (ctype.name, ctype.name))
            elif isinstance(ctype, CFunctionType):
                postponed.setdefault(name, [])
                write_function(ctype.name)

        for type_name in sorted(context.type_node_map['funcpointer'].keys()):
            fn_type = context.ctypes_map[type_name]
            write_function(fn_type.name)
        for lines in postponed.values():
            code.extend(lines)
        code.append('')
        for fn_name in fn_list:
            code.append(fn_code_map[fn_name])
        code.append('')
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if
            value in context.type_node_map['funcpointer']}
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        code.append('__all__ = [')
        for fn_name in sorted(done.union(set(alias.keys()))):
            code.append('    %r,' % fn_name)
        code.extend([']', ''])
        return linesep.join(code)

    def _generate_enum_init_source(self, context: Context):
        code = []
        for enum_name in sorted(context.enum_map.keys()):
            code.append('from ._vulkan_enum.%s import %s' % (enum_name, enum_name))
        code.append('')
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in context.enum_map}
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)

    def _generate_type_init_source(self, context: Context):
        code = []
        for type_name in sorted(context.type_node_map['complex'].keys()):
            code.append('from ._vulkan_type.%s import %s' % (type_name, type_name))
        code.append('')
        alias = {
            name: value for name, value in {
                name: context.resolve_alias(name) for name in context.alias_map
            }.items() if value in context.type_node_map['complex']
        }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)

    def _generate_procedure_init_source(self, context: Context):
        code = []
        for name in sorted(context.command_map.keys()):
            code.append('from ._vulkan_procedure.%s import %s' % (name, name))
        code.append('')
        alias = {name: value for name, value in {name: context.resolve_alias(name) for name in context.alias_map}.items() if value in context.command_map}
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)

    def _generate_error_source(self, context: Context):
        code = [
            'from ._vulkan_enum.VkResult import VkResult',
            '',
            'class VkException(Exception):',
            '    from_code = {}',
            '',
            '    @classmethod',
            '    def check(cls, code: VkResult|int):',
            '        if code != VkResult.VK_SUCCESS:',
            '            if code in cls.from_code:',
            '                raise cls.from_code[code]',
            '            raise cls(str(code))',
            '',
            'class VkError(VkException):',
            '    pass',
            '',
            'class VkStatus(VkException):',
            '    pass',
            ''
        ]
        exception_by_code = {}
        for error_name in sorted(context.enum_map['VkResult']['values']):
            error_words = error_name.split('_')
            class_name = []
            error_words = [w for w in error_words if w.upper() != 'ERROR']
            for word in error_name.split('_'):
                if word in context.tag_set or word.upper() == 'ERROR':
                    continue
                class_name.append(word[:1].upper() + word[1:].lower())
            error_value = context.value_map[error_name]['value']
            base_class = 'VkStatus'
            if error_value < 0:
                class_name.append('Error')
                base_class = 'VkError'
            if error_value == 0:
                continue
            class_name = ''.join(class_name)
            code.extend(
                [
                    'class %s(%s):' % (class_name, base_class),
                    '    code = %r' % error_value,
                    ''
                ]
            )
            exception_by_code[error_value] = class_name
        for error_code, class_name in exception_by_code.items():
            code.append('VkException.from_code[%d] = %s' % (error_code, class_name))
        code.append('')
        code.append('__all__ = [')
        code.append('    %r,' % 'VkException')
        code.append('    %r,' % 'VkError')
        code.append('    %r,' % 'VkStatus')
        for error_name in sorted(exception_by_code.values()):
            code.append('    %r,' % error_name)
        code.append(']')
        code.append('')
        return linesep.join(code)

    def _generate_handle_source(self, context: Context):
        code = ['import ctypes', '']
        for name in sorted(context.type_node_map['handle']):
            ctype = context.ctypes_map[name]
            code.append('%s = %s' % (name, ctype.to_source()))
        code.extend(['', '__all__ = ['])
        for name in sorted(context.type_node_map['handle']):
            code.append('    %r,' % name)
        code.extend([']', ''])
        return linesep.join(code)

    def generate(self, context: Context):
        self.base_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        source = self._generate_base_source(context)
        with open(self.base_dir.joinpath('vulkan_base.py'), 'w') as file:
            file.write(source)
        enum_dir = self.base_dir.joinpath('_vulkan_enum')
        enum_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        for name in context.enum_map.keys():
            filename = enum_dir.joinpath(name + '.py')
            source = self._generate_enum_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_enum_init_source(context)
        with open(self.base_dir.joinpath('vulkan_enum.py'), 'w') as file:
            file.write(source)
        source = self._generate_value_source(context)
        with open(self.base_dir.joinpath('vulkan_value.py'), 'w') as file:
            file.write(source)
        callback_dir = self.base_dir.joinpath('_vulkan_callback')
        callback_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        for name in [context.ctypes_map[k].name for k in context.type_node_map['funcpointer'].keys()]:
            filename = callback_dir.joinpath('%s.py' % name)
            source = self._generate_function_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        descriptor_dir = self.base_dir.joinpath('_descriptor')
        descriptor_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        for name in [context.ctypes_map[k].name for k in context.type_node_map['funcpointer'].keys()]:
            filename = descriptor_dir.joinpath('%s.py' % name)
            source = self._generate_callback_descriptor_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        for name in context.type_node_map['complex']:
            filename = descriptor_dir.joinpath('%s.py' % name)
            source = self._generate_complex_descriptor_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        for name in context.command_map:
            filename = descriptor_dir.joinpath('%s.py' % name)
            source = self._generate_procedure_descriptor_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_callback_init_source(context)
        with open(self.base_dir.joinpath('vulkan_callback.py'), 'w') as file:
            file.write(source)
        type_dir = self.base_dir.joinpath('_vulkan_type')
        type_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        for name in context.type_node_map['complex'].keys():
            filename = type_dir.joinpath(name + '.py')
            source = self._generate_complex_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_type_init_source(context)
        with open(self.base_dir.joinpath('vulkan_type.py'), 'w') as file:
            file.write(source)
        source = self._generate_handle_source(context)
        with open(self.base_dir.joinpath('vulkan_handle.py'), 'w') as file:
            file.write(source)
        command_dir = self.base_dir.joinpath('_vulkan_procedure')
        command_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        for name in context.command_map:
            filename = command_dir.joinpath('%s.py' % name)
            source = self._generate_procedure_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_procedure_init_source(context)
        with open(self.base_dir.joinpath('vulkan_procedure.py'), 'w') as file:
            file.write(source)
        source = self._generate_error_source(context)
        with open(self.base_dir.joinpath('vulkan_error.py'), 'w') as file:
            file.write(source)
