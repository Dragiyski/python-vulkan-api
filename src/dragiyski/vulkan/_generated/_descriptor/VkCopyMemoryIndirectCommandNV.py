from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyMemoryIndirectCommandNV'
_member_list_ = ['srcAddress', 'dstAddress', 'size']
_member_info_ = {
    'srcAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'dstAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
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
