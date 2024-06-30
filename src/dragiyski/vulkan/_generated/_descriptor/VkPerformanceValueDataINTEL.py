from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkPerformanceValueDataINTEL'
_member_list_ = ['value32', 'value64', 'valueFloat', 'valueBool', 'valueString']
_member_info_ = {
    'value32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'value64': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'valueFloat': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'valueBool': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'valueString': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPerformanceValueINTEL',
}
_input_of_ = set()
_output_of_ = set()
