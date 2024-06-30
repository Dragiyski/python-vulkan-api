from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAcquireNextImageInfoKHR'
_member_list_ = ['sType', 'pNext', 'swapchain', 'timeout', 'semaphore', 'fence', 'deviceMask']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'swapchain': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'timeout': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'semaphore': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'fence': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'deviceMask': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkAcquireNextImage2KHR',
}
_output_of_ = set()
