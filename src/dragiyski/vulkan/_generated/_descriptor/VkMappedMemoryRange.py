from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMappedMemoryRange'
_member_list_ = ['sType', 'pNext', 'memory', 'offset', 'size']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MAPPED_MEMORY_RANGE',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'offset': {
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
    'vkFlushMappedMemoryRanges',
    'vkInvalidateMappedMemoryRanges',
}
_output_of_ = set()
