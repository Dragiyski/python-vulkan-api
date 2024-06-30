from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkNativeBufferUsage2ANDROID'
_member_list_ = ['consumer', 'producer']
_member_info_ = {
    'consumer': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'producer': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
