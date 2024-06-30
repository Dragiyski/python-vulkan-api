from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkPerformanceCounterResultKHR'
_member_list_ = ['int32', 'int64', 'uint32', 'uint64', 'float32', 'float64']
_member_info_ = {
    'int32': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'int64': {
        'type': CIntType('c_int64'),
        'is_string': False,
    },
    'uint32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'uint64': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'float32': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'float64': {
        'type': CFloatType('c_double'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
