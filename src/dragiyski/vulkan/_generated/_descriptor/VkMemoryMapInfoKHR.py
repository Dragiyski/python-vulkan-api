from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryMapInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'memory', 'offset', 'size']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_MAP_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkMemoryMapFlags',
        'enum': 'VkMemoryMapFlags',
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
_extended_by_ = {
    'VkMemoryMapPlacedInfoEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkMapMemory2KHR',
}
_output_of_ = set()
