from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryAllocateFlagsInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'deviceMask']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_ALLOCATE_FLAGS_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkMemoryAllocateFlags',
        'enum': 'VkMemoryAllocateFlags',
        'is_string': False,
    },
    'deviceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkMemoryAllocateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
