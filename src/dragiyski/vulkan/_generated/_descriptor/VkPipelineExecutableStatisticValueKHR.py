from ..._ctypes import *

_category_ = 'union'
_name_ = 'VkPipelineExecutableStatisticValueKHR'
_member_list_ = ['b32', 'i64', 'u64', 'f64']
_member_info_ = {
    'b32': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'i64': {
        'type': CIntType('c_int64'),
        'is_string': False,
    },
    'u64': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'f64': {
        'type': CFloatType('c_double'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPipelineExecutableStatisticKHR',
}
_input_of_ = set()
_output_of_ = set()
