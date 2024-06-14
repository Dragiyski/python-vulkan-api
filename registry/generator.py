import ctypes
from pathlib import Path
from .context import Context
from .platform import CPlainType
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

    def generate_base_source(self, context: Context):
        code = ['import ctypes', 'from enum import IntEnum, IntFlag', '']
        for enum_class in ['enum', 'bitmask']:
            for ctype, descriptor in context.plain_ctype_class[enum_class].items():
                code.extend([
                    'class %s(%s):' % (descriptor['class_name'], descriptor['base_class_name']),
                    '    def __init__(self, *args, **kwargs):',
                    '        self._as_parameter_ = ctypes.%s(%s(self))' % (ctype.__name__, descriptor['python_type']),
                    '', ''
                ])
            code.append('Vulkan%s = {' % enum_class_suffix[enum_class])
            for ctype, descriptor in context.plain_ctype_class[enum_class].items():
                code.append('    ctypes.%s: %s,' % (ctype.__name__, descriptor['class_name']))
            code.extend(['}', ''])
        for ctype, descriptor in context.plain_ctype_class['value'].items():
            code.extend([
                'class %s(%s):' % (descriptor['class_name'], descriptor['python_type']),
                '    def __new__(cls, *args, **kwargs):',
                '        value = super().__new__(cls, *args, **kwargs)',
                '        value._as_parameter_ = ctypes.%s(%s(value))' % (ctype.__name__, descriptor['python_type']),
                '        return value',
                '', ''
            ])
        code.append('VulkanValue = {')
        for ctype, descriptor in context.plain_ctype_class['value'].items():
            code.append('    ctypes.%s: %s,' % (ctype.__name__, descriptor['class_name']))
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
        return linesep.join(code)

    def generate_enum_source(self, context: Context, name: str):
        if name not in context.enum_map:
            raise GeneratorError('No enum named "%s" found.' % name, name=name)
        descriptor = context.enum_map[name]
        type_descriptor = context.plain_ctype_class[descriptor['class']][descriptor['ctype'].ctype()]
        code = ['import ctypes, sys', 'from .._vulkan_base import %s' % type_descriptor['class_name'], '']
        code.append('class %s(%s):' % (name, type_descriptor['class_name']))
        value_count = len(descriptor['values'])
        if value_count > 0:
            for value_name in descriptor['values']:
                value_descriptor = context.value_map[value_name]
                code.append('    %s = %r' % (value_name, value_descriptor['value']))
        else:
            code.append('    pass')
        code.append('')
        code.append('sys.modules[__name__] = %s' % name)
        code.append('')
        return linesep.join(code)
    
    def generate_value_source(self, context: Context):
        code = []
        enum_set = set()
        for descriptor in context.value_map.values():
            if 'enum_name' in descriptor:
                enum_set.add(descriptor['enum_name'])
        for enum_name in enum_set:
            code.append('from .vulkan_enum import %s' % enum_name)
        code.append('')
        for name, descriptor in context.value_map.items():
            if 'enum_name' in descriptor:
                code.append('%s = %s.%s' % (name, descriptor['enum_name'], name))
            else:
                code.append('%s = %r' % (name, descriptor['value']))
        code.append('')
        return linesep.join(code)
