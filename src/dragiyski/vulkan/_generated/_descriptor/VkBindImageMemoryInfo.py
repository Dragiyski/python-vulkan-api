from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBindImageMemoryInfo'
_member_list_ = ['sType', 'pNext', 'image', 'memory', 'memoryOffset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'image': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkBindImageMemoryDeviceGroupInfo',
    'VkBindImageMemorySwapchainInfoKHR',
    'VkBindImagePlaneMemoryInfo',
    'VkBindMemoryStatusKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkBindImageMemory2',
}
_output_of_ = set()
