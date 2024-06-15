import ctypes
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
        code = ['import ctypes, sys', 'from .._vulkan_base import %s' % type_descriptor['class_name'], '']
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
        code = []
        enum_set = set()
        for descriptor in context.value_map.values():
            if 'enum_name' in descriptor:
                enum_set.add(descriptor['enum_name'])
        code.append('from ._enum import (')
        for enum_name in sorted(enum_set):
            code.append('    %s,' % enum_name)
        code.append(')')
        value_map = {}
        for name, descriptor in context.value_map.items():
            if 'enum_name' in descriptor:
                value_map[name] = '%s = %s.%s' % (name, descriptor['enum_name'], name)
            else:
                value_map[name] = '%s = %r' % (name, descriptor['value'])
        for name in sorted(value_map.keys()):
            code.append(value_map[name])
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in context.value_map }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        code.append('__all__ = [')
        for name in sorted(list(value_map.keys()) + list(alias.keys())):
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
                code.append('from .._vulkan_callback import %s' % ', '.join([context.ctypes_map[t].deref().name for t in funcpointer_member_types]))
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
        code = ['import ctypes', 'from ._vulkan_base import VKAPI_PTR, VKAPI_CALL']
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
            code.append('from ._struct import (')
            for dep_name in sorted(dep_map['struct']):
                code.append('    %s,' % dep_name)
            code.append(')')
        if 'callback' in dep_map and len(dep_map['callback']) > 0:
            code.append('from ._vulkan_callback import (')
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
        code = ['import ctypes', 'from ._vulkan_base import VKAPI_PTR, VKAPI_CALL']
        fn_code_map = {}
        fn_list = []
        def check_type_dep(ctype):
            if isinstance(ctype, CPointerType):
                check_type_dep(ctype.deref())
            elif isinstance(ctype, CArrayType):
                check_type_dep(ctype.item_ctype)
            elif isinstance(ctype, CComplexType):
                code.append('from ._struct import %s' % ctype.name)
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
        code = ['from ._enum import (']
        for enum_name in sorted(context.enum_map.keys()):
            code.append('    %s,' % enum_name)
        code.extend([')', ''])
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in context.enum_map }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)
    
    def _generate_struct_public_source(self, context: Context):
        code = ['from ._struct import (']
        for enum_name in sorted(context.enum_map.keys()):
            code.append('    %s,' % enum_name)
        code.extend([')', ''])
        alias = { name: value for name, value in { name: context.resolve_alias(name) for name in context.alias_map }.items() if value in context.type_node_map['complex'] }
        for name in sorted(alias.keys()):
            code.append('%s = %s' % (name, alias[name]))
        code.append('')
        return linesep.join(code)
    
    def _generate_init_source(self, context: Context):
        code = [
            'from ._vulkan_base import *',
            'from ._vulkan_callback import *',
            'from .command import *',
            'from .enum import *',
            'from .const import *',
            'from .struct import *',
            ''
        ]
        return linesep.join(code)
    
    def generate(self, context: Context):
        self.base_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        source = self._generate_base_source(context)
        with open(self.base_dir.joinpath('_vulkan_base.py'), 'w') as file:
            file.write(source)
        enum_dir = self.base_dir.joinpath('_enum')
        enum_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        for name in context.enum_map.keys():
            filename = enum_dir.joinpath(name + '.py')
            source = self._generate_enum_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_enum_public_source(context)
        with open(self.base_dir.joinpath('enum.py'), 'w') as file:
            file.write(source)
        source = self._generate_value_source(context)
        with open(self.base_dir.joinpath('const.py'), 'w') as file:
            file.write(source)
        source = self._generate_funcpointer_source(context)
        with open(self.base_dir.joinpath('_vulkan_callback.py'), 'w') as file:
            file.write(source)
        struct_dir = self.base_dir.joinpath('_struct')
        struct_dir.mkdir(mode=0o755, parents=True, exist_ok=True)
        for name in context.type_node_map['complex'].keys():
            filename = struct_dir.joinpath(name + '.py')
            source = self._generate_complex_source(context, name)
            with open(filename, 'w') as file:
                file.write(source)
        source = self._generate_struct_public_source(context)
        with open(self.base_dir.joinpath('struct.py'), 'w') as file:
            file.write(source)
        source = self._generate_command_source(context)
        with open(self.base_dir.joinpath('command.py'), 'w') as file:
            file.write(source)
        source = self._generate_init_source(context)
        with open(self.base_dir.joinpath('__init__.py'), 'w') as file:
            file.write(source)
