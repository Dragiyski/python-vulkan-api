from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferCopy2'
_member_list_ = ['sType', 'pNext', 'srcOffset', 'dstOffset', 'size']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_COPY_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
_included_in_ = {
    'VkCopyBufferInfo2',
}
_input_of_ = set()
_output_of_ = set()
