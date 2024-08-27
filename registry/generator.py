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
        code = ['import ctypes', 'from .._function_type import VKAPI_PTR, VKAPI_CALL']
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
        code = [
            'import ctypes',
            'from ..._function_type import %s' % (ctype.constructor),
            'from ..._ctypes import *',
            ''
        ]

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
        code.append('%s._vulkan_ctype_ = %s' % (ctype.name, ctype.get_runtime_source()))
        return code

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
        code = ['import ctypes', 'from .._function_type import VKAPI_PTR, VKAPI_CALL']
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
    
    def _create_function_source(self, context: Context, name: str, dep_map: dict):
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

        ctype = context.ctypes_map[name]
        code = []
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
        code.append('%s._vulkan_ctype_ = %s' % (ctype.name, ctype.get_runtime_source()))
        code.append('%s._vulkan_ctype_._class_ = %s' % (ctype.name, ctype.name))
        return code

    
    def _write_vulkan_database(self, context: Context):
        source = ['vendor_suffix = %r' % (list(sorted(context.tag_set))), '']
        file_path = self.base_dir.joinpath('_vulkan_database.py')
        with open(file_path, 'w') as file:
            file.write(linesep.join(source))

    def _write_vulkan_enum(self, context: Context, enum_name: str):
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
        code.append('%s.__doc__ = %r' % (enum_name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % enum_name))
        code.append('')
        file = self.base_dir.joinpath('_vulkan_enum/%s.py' % enum_name)
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_enums(self, context: Context):
        if len(context.enum_map) <= 0:
            return
        code = []
        deps = []
        for enum_name in context.enum_map:
            self._write_vulkan_enum(context, enum_name)
            deps.append(enum_name)
        for enum_name in sorted(deps):
            code.append('from .%s import %s' % (enum_name, enum_name))
        code.append('')
        alias_enum = { k: v for k, v in context.alias_map.items() if v in context.enum_map }
        for alias_name in sorted(alias_enum.keys()):
            enum_name = alias_enum[alias_name]
            code.append('%s = %s' % (alias_name, enum_name))
        code.append('')
        file = self.base_dir.joinpath('_vulkan_enum/__init__.py')
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_value(self, context: Context):
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
        file = self.base_dir.joinpath('_vulkan_value.py')
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_callback(self, context: Context, name: str):
        dep_map = {}
        code = ['import ctypes', 'from ..._ctypes import *']
        fn_code = self._create_function_source(context, name, dep_map)
        if 'struct' in dep_map and len(dep_map['struct']) > 0:
            for dep_name in sorted(dep_map['struct']):
                code.append('from .._vulkan_type.%s import %s' % (dep_name, dep_name))
        if 'callback' in dep_map and len(dep_map['callback']) > 0:
            for dep_name in sorted(dep_map['callback']):
                code.append('from .%s import %s' % (dep_name, dep_name))
        code.append('')
        code.extend(fn_code)
        code.append('%s.__doc__ = %r' % (name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % name))
        info = context.callback_map[f'PFN_{name}']
        code.append('%s._vulkan_ctype_.return_type = %s' % (name, info['return'].get_runtime_source()))
        for arg_index, arg_name in enumerate(info['arg_list']):
            arg_type = info['arg_map'][arg_name]
            info['node'].children['type'][arg_index]
            code.append('%s._vulkan_ctype_.arguments[%r] = %s' % (name, arg_name, arg_type.get_runtime_source()))
        code.append('')
        file = self.base_dir.joinpath('_vulkan_callback/%s.py' % name)
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))
    
    def _write_vulkan_callbacks(self, context: Context):
        code = []
        for name in [context.ctypes_map[k].name for k in context.type_node_map['funcpointer'].keys()]:
            self._write_vulkan_callback(context, name)
            code.append('from .%s import %s' % (name, name))
        code.append('')

        file = self.base_dir.joinpath('_vulkan_callback/__init__.py')
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))
    
    def _write_vulkan_type(self, context: Context, name: str):
        code = ['import ctypes', 'from ..._ctypes import *', '']
        ctype = context.ctypes_map[name]
        ctype: CComplexType
        info = context.struct_map[name]

        def generate_class_body():
            return False

        code.append('class %s(ctypes.%s):' % (name, ctype.constructor))
        member_types = [ctype.member_map[x]['node'].get('type').get_text() for x in ctype.member_list]
        complex_member_types = set([x for x in member_types if x in context.type_node_map['complex']])
        funcpointer_member_types = set([x for x in member_types if x in context.type_node_map['funcpointer']])
        delay_fields = ctype['delay_fields'] or name in complex_member_types or name in funcpointer_member_types
        in_class_body = True
        if delay_fields or len(complex_member_types) > 0 or len(funcpointer_member_types) > 0:
            if not generate_class_body():
                code.append('    pass')
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
        code.append('%s.__doc__ = %r' % (name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % name))
        code.append('')
        if in_class_body:
            generate_class_body()
        members = OrderedDict()
        member_deps = {
            'enum': set(),
            'value': set()
        }
        for member_name in ctype.member_list:
            member_info = ctype.member_map[member_name]
            member_code = ['    %r: {' % member_name]
            member_type = member_info['node'].get('type').get_text()
            member_type_class = 'ctypes'
            if member_type in context.enum_map:
                member_type_class = 'enum'
                member_deps['enum'].add(member_type)
                member_code.append('        %r: %s,' % ('enum', member_type))
            elif member_type in context.type_node_map['complex']:
                member_type_class = context.ctypes_map[member_type].constructor.lower()
            elif member_type in context.type_node_map['funcpointer']:
                member_type_class = 'callback'
            elif member_type in context.type_node_map['handle']:
                member_type_class = 'handle'
            member_code.append('        %r: %r,' % ('type', {
                'class': member_type_class,
                'name': member_type
            }))
            if member_info['node'].has_attribute('values'):
                member_value = member_info['node'].attributes['values']
                if member_value in context.value_map:
                    member_deps['value'].add(member_value)
                    member_code.append('        %r: %s,' % ('value', member_value))
            members[member_name] = member_code
            if member_info['node'].has_attribute('selection'):
                assert ctype.constructor == 'Union'
                member_selection = member_info['node'].attributes['selection']
                if member_selection in context.value_map:
                    member_deps['value'].add(member_selection)
                    member_code.append('        %r: %s,' % ('selection', member_selection))
            if member_info['node'].has_attribute('selector'):
                member_selector = member_info['node'].attributes['selector']
                assert member_selector in ctype.member_list
                member_code.append('        %r: %r,' % ('selector', member_selector))
            if member_info['node'].has_attribute('len'):
                member_len = member_info['node'].attributes['len']
                if member_len.startswith('latexmath:'):
                    assert member_info['node'].has_attribute('altlen')
                    member_len = member_info['node'].attributes['altlen']
                member_len = [x.replace('->', '.') for x in member_len.split(',')]
                member_code.append('        %r: %r,' % ('length', member_len))
            member_externsync = False
            if member_info['node'].has_attribute('externsync'):
                assert member_info['node'].attributes['externsync'].lower() == 'true'
                member_externsync = True
            member_code.append('        %r: %r,' % ('sync', member_externsync))
            if member_info['node'].has_attribute('objecttype'):
                # This should be only applied to uint64_t type.
                # The field specified in objecttype specify type of handle, while the uint64_t specify the value of the handle, if any.
                member_objecttype = member_info['node'].attributes['objecttype']
                assert member_objecttype in ctype.member_list
                member_code.append('        %r: %r,' % ('handle_type', member_objecttype))
            if member_info['node'].has_attribute('limittype'):
                member_limittype = member_info['node'].attributes['limittype']
                member_code.append('        %r: %r,' % ('limit_function', member_limittype))
            member_code.append('    },')
            members[member_name] = member_code

        if len(member_deps['enum']) > 0 or len(member_deps['value']) > 0:
            code.append('')
            if len(member_deps['enum']) > 0:
                code.append('from .._vulkan_enum import %s' % ', '.join(sorted(member_deps['enum'])))
            if len(member_deps['value']) > 0:
                code.append('from .._vulkan_value import %s' % ', '.join(sorted(member_deps['value'])))
        code.append('')

        code.append('%s._vulkan_ctype_ = %s' % (name, ctype.get_runtime_source()))
        code.append('%s._vulkan_ctype_._class_ = %s' % (name, name))
        for member_name in ctype.member_list:
            code.append('%s._vulkan_ctype_.fields[%r] = %s' % (
                name,
                member_name,
                ctype.member_map[member_name]['ctype'].get_runtime_source()
            ))

        code.append('%s._vulkan_fields_ = {' % name)
        for member_code in members.values():
            code.extend(member_code)
        code.append('}')
        code.append('')

        file = self.base_dir.joinpath('_vulkan_type/%s.py' % (name))
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_types(self, context: Context):
        code = []
        deps = []
        for name in context.type_node_map['complex']:
            self._write_vulkan_type(context, name)
            deps.append(name)
        for name in sorted(deps):
            code.append('from .%s import %s' % (name, name))
        alias_map = { k: v for k, v in context.alias_map.items() if v in context.type_node_map['complex'] }
        for alias_name in sorted(alias_map.keys()):
            type_name = alias_map[alias_name]
            code.append('%s = %s' % (alias_name, type_name))
        file = self.base_dir.joinpath('_vulkan_type/__init__.py')
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_handles(self, context: Context):
        code = ['from .._ctypes import *', '']
        for handle_name in context.handle_map:
            handle_info = context.handle_map[handle_name]
            code.append('%s = %s' % (handle_name, handle_info['ctype'].get_runtime_source()))
        code.append('')
        for handle_name in context.handle_map:
            handle_info = context.handle_map[handle_name]
            is_dispatchable = handle_info['typedef'] != 'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
            code.append('%s.dispatchable = %r' % (handle_name, is_dispatchable))
            if 'parent' in handle_info and isinstance(handle_info['parent'], str):
                code.append('%s.parent = %s' % (handle_name, handle_info['parent']))
        code.append('')

        handle_alias = { k: v for k, v in context.alias_map.items() if v in context.handle_map }
        for alias_name, handle_name in handle_alias.items():
            code.append('%s = %s' % (alias_name, handle_name))
        code.append('')
        
        file = self.base_dir.joinpath('_vulkan_handle.py')
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def _write_vulkan_command(self, context: Context, name: str):
        ctype = context.ctypes_map[name]
        info = context.command_map[name]
        dep_map = { 'enum': set() }
        code = ['import ctypes', 'from collections import OrderedDict', 'from ..._ctypes import *']
        fn_code = self._create_function_source(context, name, dep_map)
        for arg_name in info['argument_list']:
            arg_info = info['argument_map'][arg_name]
            arg_type = arg_info['type']
            if arg_type in context.enum_map:
                dep_map['enum'].add(arg_type)
            if arg_info['node'].has_attribute('validstructs'):
                arg_valid_struct_list = [x.strip() for x in arg_info['node'].get_attribute('validstructs').split(',')]
                for arg_struct in arg_valid_struct_list:
                    arg_struct = context.resolve_alias(arg_struct)
                    assert arg_struct in context.type_node_map['complex'] and arg_struct in context.ctypes_map
                    assert tuple(context.ctypes_map[arg_struct].member_list[:2]) == ('sType', 'pNext')
                    dep_map['struct'].add(arg_struct)
        if 'struct' in dep_map and len(dep_map['struct']) > 0:
            for dep_name in sorted(dep_map['struct']):
                code.append('from .._vulkan_type.%s import %s' % (dep_name, dep_name))
        if 'callback' in dep_map and len(dep_map['callback']) > 0:
            for dep_name in sorted(dep_map['callback']):
                code.append('from .._vulkan_callback.%s import %s' % (dep_name, dep_name))
        if 'enum' in dep_map and len(dep_map['enum']) > 0:
            for dep_name in sorted(dep_map['enum']):
                code.append('from .._vulkan_enum.%s import %s' % (dep_name, dep_name))
        code.append('')
        return_status = info['return']['type'] == 'VkResult'
        if return_status:
            code.append('from .._vulkan_enum.VkResult import VkResult')
        code.extend(fn_code)
        code.append('%s.__doc__ = %r' % (name, 'https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/%s.html' % name))
        code.append('%s._vulkan_ctype_.return_type = %s' % (name, info['return']['ctype'].get_runtime_source()))
        for arg_name in info['argument_list']:
            arg_type = info['argument_map'][arg_name]['ctype']
            code.append('%s._vulkan_ctype_.arguments[%r] = %s' % (name, arg_name, arg_type.get_runtime_source()))
        code.append('')
        if return_status or info['return']['type'] == 'void':
            return_arguments = [arg_name for arg_name in info['argument_list'] if info['argument_map'][arg_name]['output']]
        else:
            return_arguments = []
        code.append('%s._vulkan_return_ = {' % name)
        code.append('    %r: %r,' % ('status', return_status))
        code.append('    %r: %r,' % ('arguments', return_arguments))
        if return_status:
            if 'success_code_list' in info:
                code.append('    %r: [%s],' % ('success', ', '.join(f'VkResult.{x}' for x in sorted(info['success_code_list']))))
            else:
                code.append('    %r: [],' % ('success'))
            if 'error_code_list' in info:
                code.append('    %r: [%s],' % ('error', ', '.join(f'VkResult.{x}' for x in sorted(info['error_code_list']))))
            else:
                code.append('    %r: [],' % ('error'))
        code.append('}')
        code.append('%s._vulkan_arguments_ = OrderedDict()' % name)
        externsync = []
        for arg_name in info['argument_list']:
            arg_code = []
            arg_info = info['argument_map'][arg_name]
            code.append('%s._vulkan_arguments_[%r] = {' % (name, arg_name))
            arg_type = arg_info['type']
            arg_type_class = 'ctypes'
            if arg_type in context.enum_map:
                arg_type_class = 'enum'
                arg_code.append('    %r: %s,' % ('enum', arg_type))
            elif arg_type in context.type_node_map['complex']:
                arg_type_class = context.ctypes_map[arg_type].constructor.lower()
            elif arg_type in context.type_node_map['funcpointer']:
                arg_type_class = 'callback'
            elif arg_type in context.type_node_map['handle']:
                arg_type_class = 'handle'
            code.append('    %r: %r,' % ('type', {
                'class': arg_type_class,
                'name': arg_type
            }))
            code.extend(arg_code)
            arg_optional = []
            if arg_info['node'].has_attribute('optional'):
                arg_optional = [x.strip().lower() == 'true' for x in arg_info['node'].get_attribute('optional').split(',')]
            if len(arg_optional) == 0:
                arg_optional.append(False)
            code.append('    %r: %r,' % ('optional', arg_optional))
            if arg_info['node'].has_attribute('externsync'):
                arg_externsync = arg_info['node'].get_attribute('externsync')
                if arg_externsync == 'true':
                    externsync.append(arg_name)
                else:
                    arg_externsync = [x.strip().replace('[]', '[:]').replace('->', '.') for x in arg_externsync.split(',')]
                    externsync.extend(arg_externsync)
            if arg_info['node'].has_attribute('len'):
                length = arg_info['node'].get_attribute('len')
                if arg_info['node'].has_attribute('altlen'):
                    length = arg_info['node'].get_attribute('altlen')
                length = [item.strip().replace('[]', '[:]').replace('->', '.') for item in length.split(',')]
                code.append('    %r: %r,' % ('length', length))
            if arg_info['node'].has_attribute('selector'):
                # Note: currently no command takes union argument, thus no command contain @selector attribute
                arg_selector = arg_info['node'].get_attribute('selector')
                code.append('    %r: %r,' % ('selector', arg_selector.strip().replace('->', '.')))
            if arg_info['node'].has_attribute('objecttype'):
                # Indicator that the current 64-bit integer type contains a handle. Its content will be the name
                # of another argument (or argument's struct member) that contain enumeration specifying the type
                # of the contained handle. The handle can be NULL, in which case the type does not matter.
                arg_objecttype = arg_info['node'].get_attribute('objecttype')
                code.append('    %r: %r,' % ('handle_type', arg_objecttype.strip().replace('->', '.')))
            if arg_info['node'].has_attribute('validstructs'):
                # In some cases the argument is an I/O of generic VkBaseInStructure or VkBaseOutStructure.
                # In such case the argument should point to one or more structures chained with pNext and determined by sType.
                # Which type of structures are supported for this parameter will be determined by the @validstructs
                arg_valid_struct_list = [x.strip() for x in arg_info['node'].get_attribute('validstructs').split(',')]
                arg_struct_set = set()
                for arg_struct in arg_valid_struct_list:
                    arg_struct = context.resolve_alias(arg_struct)
                    arg_struct_set.add(arg_struct)
                code.append('    %r: {%r},' % ('structure_type', ', '.join(sorted(arg_struct_set))))
            code.append('}')
        if len(externsync) > 0:
            code.append('%s._vulkan_sync_ = [' % name)
            for sname in externsync:
                code.append('    %r,' % sname)
            code.append(']')
        else:
            code.append('%s._vulkan_sync_ = []' % name)
        doc_text = []
        if 'implicitexternsyncparams' in info['node'].children:
            for sync_doc in info['node'].get_all('implicitexternsyncparams'):
                for sync_doc_param in sync_doc.get_all('param'):
                    sync_doc_param_text = sync_doc_param.get_text().strip()
                    if len(sync_doc_param_text) > 0:
                        doc_text.append(sync_doc_param_text)
        if len(doc_text) > 0:
            code.append('%s._vulkan_sync_doc_ = [' % name)
            for doc_entry in doc_text:
                code.append('    %r,' % doc_entry)
            code.append(']')
        else:
            code.append('%s._vulkan_sync_doc_ = []' % name)
        code.append('')

        file = self.base_dir.joinpath('_vulkan_command/%s.py' % (name))
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))


    def _write_vulkan_commands(self, context: Context):
        code = []
        for name in context.command_map:
            self._write_vulkan_command(context, name)
            code.append('from .%s import %s' % (name, name))
        alias_map = { k: v for k, v in context.alias_map.items() if v in context.command_map }
        for alias_name in sorted(alias_map.keys()):
            name = alias_map[alias_name]
            code.append('%s = %s' % (alias_name, name))
        code.append('')

        file = self.base_dir.joinpath('_vulkan_command/__init__.py')
        file.parent.mkdir(mode = 0o755, parents = True, exist_ok = True)
        with open(file, 'w') as stream:
            stream.write(linesep.join(code))

    def generate(self, context: Context):
        self.base_dir.mkdir(mode = 0o755, parents = True, exist_ok = True)
        self._write_vulkan_database(context)
        self._write_vulkan_enums(context)
        self._write_vulkan_value(context)
        self._write_vulkan_callbacks(context)
        self._write_vulkan_types(context)
        self._write_vulkan_handles(context)
        self._write_vulkan_commands(context)
