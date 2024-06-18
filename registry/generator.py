import ctypes
import ast
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
            plain_type_map = { k.__name__: v for k, v in context.plain_ctype_class[enum_class].items() }
            for ctype_name in sorted(plain_type_map.keys()):
                descriptor = plain_type_map[ctype_name]
                exports.append(descriptor['class_name'])
                code.extend([
                    'class %s(%s):' % (descriptor['class_name'], descriptor['base_class_name']),
                    '    def __init__(self, *args, **kwargs):',
                    '        self._as_parameter_ = ctypes.%s(%s(self))' % (ctype_name, descriptor['python_type']),
                    '', ''
                ])
            code.append('Vulkan%s = {' % enum_class_suffix[enum_class])
            for ctype_name in sorted(plain_type_map.keys()):
                descriptor = plain_type_map[ctype_name]
                code.append('    ctypes.%s: %s,' % (ctype_name, descriptor['class_name']))
            code.extend(['}', ''])
        plain_type_map = { k.__name__: v for k, v in context.plain_ctype_class['value'].items() }
        for ctype_name in sorted(plain_type_map.keys()):
            descriptor = plain_type_map[ctype_name]
            exports.append(descriptor['class_name'])
            code.extend([
                'class %s(%s):' % (descriptor['class_name'], descriptor['python_type']),
                '    def __new__(cls, *args, **kwargs):',
                '        value = super().__new__(cls, *args, **kwargs)',
                '        value._as_parameter_ = ctypes.%s(%s(value))' % (ctype_name, descriptor['python_type']),
                '        return value',
                '', ''
            ])
        code.append('VulkanValue = {')
        for ctype_name in sorted(plain_type_map.keys()):
            descriptor = plain_type_map[ctype_name]
            code.append('    ctypes.%s: %s,' % (ctype_name, descriptor['class_name']))
        code.extend(['}', ''])

        code.extend([
            "if hasattr(ctypes, 'WINFUNCTYPE'):",
            '    VKAPI_CALL = ctypes.WINFUNCTYPE',
            '    VKAPI_PTR = ctypes.WINFUNCTYPE',
            'else:',
            '    VKAPI_CALL = ctypes.CFUNCTYPE',
            '    VKAPI_PTR = ctypes.CFUNCTYPE',
            ''
        ])
        exports.extend(['VKAPI_CALL', 'VKAPI_PTR'])
        code.append('__all__ = [')
        for name in sorted(exports):
            code.append('    %r,' % name)
        code.extend([']', ''])
        return linesep.join(code)

    def _generate_enum_source(self, context: Context, enum_name: str):
        if enum_name not in context.enum_map:
            raise GeneratorError('No enum named "%s" found.' % enum_name, name=enum_name)
        descriptor = context.enum_map[enum_name]
        type_descriptor = context.plain_ctype_class[descriptor['class']][descriptor['ctype'].ctype()]
        code = ['import ctypes, sys', 'from ..vulkan_base import %s' % type_descriptor['class_name'], '']
        code.append('class %s(%s):' % (enum_name, type_descriptor['class_name']))
        value_count = len(descriptor['values'])
        values = {}
        for value_name in descriptor['values']:
            value_descriptor = context.value_map[value_name]
            values[value_name] = '    %s = %r' % (value_name, value_descriptor['value'])
        if len(values) > 0:
            for value_name in sorted(values.keys()):
                code.append(values[value_name])
        else:
            code.append('    pass')
        code.append('')
        code.append('sys.modules[__name__] = %s' % enum_name)
        code.append('')
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in values }
        for name in sorted(alias.keys()):
            value = alias[name]
            code.append('%s.%s = %s.%s' % (enum_name, name, enum_name, value))
        code.append('')
        return linesep.join(code)
    
    def _generate_value_source(self, context: Context):
        code = ['import ctypes']
        enum_set = set()
        exports = set()
        for descriptor in context.value_map.values():
            if 'enum_name' in descriptor:
                enum_set.add(descriptor['enum_name'])
        code.append('from ._vulkan_enum import (')
        for enum_name in sorted(enum_set):
            code.append('    %s,' % enum_name)
        code.append(')')
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
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in context.value_map }
        for name in sorted(alias.keys()):
            exports.add(name)
            code.append('%s = %s' % (name, alias[name]))
        code.append('__all__ = [')
        for name in sorted(exports):
            code.append('    %r,' % name)
        code.extend([']', ''])
        return linesep.join(code)

    def _generate_complex_source(self, context: Context, name: str):
        code = ['import ctypes, sys', '']
        ctype = context.ctypes_map[name]
        code.append('class %s(ctypes.%s):' % (name, ctype.constructor))
        member_types = [ctype.member_map[x]['node'].get('type').get_text() for x in ctype.member_list]
        complex_member_types = set([x for x in member_types if x in context.type_node_map['complex']])
        funcpointer_member_types = set([x for x in member_types if x in context.type_node_map['funcpointer']])
        delay_fields = ctype['delay_fields'] or name in complex_member_types
        if delay_fields or len(complex_member_types) > 0 or len(funcpointer_member_types) > 0:
            code.extend([
                '    pass',
                '',
                'sys.modules[__name__] = %s' % name,
                ''
            ])
            if len(funcpointer_member_types) > 0:
                code.append('from ..vulkan_callback import %s' % ', '.join(sorted([context.ctypes_map[t].deref().name for t in funcpointer_member_types])))
            for dependency in sorted(complex_member_types):
                if dependency != name:
                    code.append('from . import %s' % dependency)
            code.extend(['', '%s._fields_ = [' % name])
            for member_name in ctype.member_list:
                member_desc = ctype.member_map[member_name]
                if 'bitsize' in member_desc:
                    code.append('    (%r, %s, %d),' % (member_name, member_desc['ctype'].to_source(), member_desc['bitsize']))
                else:
                    code.append('    (%r, %s),' % (member_name, member_desc['ctype'].to_source()))
            code.extend([']', ''])
        else:
            code.append('    _fields_ = [')
            for member_name in ctype.member_list:
                member_desc = ctype.member_map[member_name]
                if 'bitsize' in member_desc:
                    code.append('        (%r, %s, %d),' % (member_name, member_desc['ctype'].to_source(), member_desc['bitsize']))
                else:
                    code.append('        (%r, %s),' % (member_name, member_desc['ctype'].to_source()))
            code.extend([
                '    ]',
                '',
                'sys.modules[__name__] = %s' % name,
                ''
            ])
        return linesep.join(code)
    
    def _generate_command_source(self, context: Context):
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
            code.append('from ._vulkan_type import (')
            for dep_name in sorted(dep_map['struct']):
                code.append('    %s,' % dep_name)
            code.append(')')
        if 'callback' in dep_map and len(dep_map['callback']) > 0:
            code.append('from .vulkan_callback import (')
            for dep_name in sorted(dep_map['callback']):
                code.append('    %s,' % dep_name)
            code.append(')')
        code.append('')
        for fn_name in fn_list:
            code.append(fn_code_map[fn_name])
        code.append('')
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in context.command_node_map }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        code.append('__all__ = [')
        for fn_name in sorted(fn_list + list(alias.keys())):
            code.append('    %r,' % fn_name)
        code.extend([']', ''])
        return linesep.join(code)
    
    def _generate_funcpointer_source(self, context: Context):
        code = ['import ctypes', 'from .vulkan_base import VKAPI_PTR, VKAPI_CALL']
        fn_code_map = {}
        fn_list = []
        def check_type_dep(ctype):
            if isinstance(ctype, CPointerType):
                check_type_dep(ctype.deref())
            elif isinstance(ctype, CArrayType):
                check_type_dep(ctype.item_ctype)
            elif isinstance(ctype, CComplexType):
                code.append('from ._vulkan_type import %s' % ctype.name)
            elif isinstance(ctype, CFunctionType):
                if ctype.name not in fn_list:
                    fn_list.append(ctype.name)
        for type_name in sorted(context.type_node_map['funcpointer'].keys()):
            ptr_type = context.ctypes_map[type_name]
            fn_type = ptr_type.deref()
            check_type_dep(fn_type.return_type)
            for arg in fn_type.argument_types:
                check_type_dep(arg)
            fn_code_map[fn_type.name] = '%s = %s(%s)' % (
                fn_type.name,
                fn_type.constructor,
                ', '.join([fn_type.return_type.to_source()] + [arg.to_source() for arg in fn_type.argument_types])
            )
            if fn_type.name not in fn_list:
                fn_list.append(fn_type.name)
        code.append('')
        for fn_name in fn_list:
            code.append(fn_code_map[fn_name])
        code.append('')
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in context.type_node_map['funcpointer'] }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        code.append('__all__ = [')
        for fn_name in sorted(fn_list + list(alias.keys())):
            code.append('    %r,' % fn_name)
        code.extend([']', ''])
        return linesep.join(code)
    
    def _generate_enum_public_source(self, context: Context):
        code = ['from ._vulkan_enum import (']
        for enum_name in sorted(context.enum_map.keys()):
            code.append('    %s,' % enum_name)
        code.extend([')', ''])
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in context.enum_map }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)
    
    def _generate_struct_public_source(self, context: Context):
        code = ['from ._vulkan_type import (']
        for enum_name in sorted(context.type_node_map['complex'].keys()):
            code.append('    %s,' % enum_name)
        code.extend([')', ''])
        alias = {
            name: value for name, value in {
                name: context.resolve_alias(name) for name in context.alias_map
            }.items() if value in context.type_node_map['complex']
        }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)
    
    def _generate_error_source(self, context: Context):
        code = [
            'class VkException(Exception):',
            '    from_code = {}',
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
            code.extend([
                'class %s(%s):' % (class_name, base_class),
                '    code = %r' % error_value,
                ''
            ])
            exception_by_code[error_value] = class_name
        for error_code, class_name in exception_by_code.items():
            code.append('VkException.from_code[%d] = %s' % (error_code, class_name))
        code.append('')
        return linesep.join(code)
    
    def _generate_command_loader_source(self, context: Context):
        code = []

        global_functions = [k for k, v in context.command_map.items() if 'handle' not in 'v']
        instance_functions = [k for k, v in context.command_map.items() if 'handle' not in 'v']
    
    def generate(self, context: Context):
        self.base_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        source = self._generate_base_source(context)
        with open(self.base_dir.joinpath('vulkan_base.py'), 'w') as file:
            file.write(source)
        enum_dir = self.base_dir.joinpath('_vulkan_enum')
        enum_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        for name in context.enum_map.keys():
            filename = enum_dir.joinpath(name + '.py')
            source = self._generate_enum_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_enum_public_source(context)
        with open(self.base_dir.joinpath('vulkan_enum.py'), 'w') as file:
            file.write(source)
        source = self._generate_value_source(context)
        with open(self.base_dir.joinpath('vulkan_value.py'), 'w') as file:
            file.write(source)
        source = self._generate_funcpointer_source(context)
        with open(self.base_dir.joinpath('vulkan_callback.py'), 'w') as file:
            file.write(source)
        struct_dir = self.base_dir.joinpath('_vulkan_type')
        struct_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        for name in context.type_node_map['complex'].keys():
            filename = struct_dir.joinpath(name + '.py')
            source = self._generate_complex_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_struct_public_source(context)
        with open(self.base_dir.joinpath('vulkan_type.py'), 'w') as file:
            file.write(source)
        source = self._generate_command_source(context)
        with open(self.base_dir.joinpath('vulkan_command.py'), 'w') as file:
            file.write(source)
        source = self._generate_error_source(context)
        with open(self.base_dir.joinpath('vulkan_error.py'), 'w') as file:
            file.write(source)
