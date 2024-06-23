import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('value32', ctypes.c_uint32),
        ('value64', ctypes.c_uint64),
        ('valueFloat', ctypes.c_float),
        ('valueBool', ctypes.c_uint32),
        ('valueString', ctypes.c_char_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPerformanceValueINTEL',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'value32': {'python_name': ['value32']},
        'value64': {'python_name': ['value64']},
        'valueFloat': {'python_name': ['value', 'float']},
        'valueBool': {'python_name': ['value', 'bool']},
        'valueString': {'python_name': ['value', 'string'], 'len': [['null-terminated']]},
    }
}
