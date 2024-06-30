from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferCopy'
_member_list_ = ['srcOffset', 'dstOffset', 'size']
_member_info_ = {
    'srcOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'dstOffset': {
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
_input_of_ = {
    'vkCmdCopyBuffer',
}
_output_of_ = set()
