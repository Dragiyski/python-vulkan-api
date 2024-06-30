from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPresentInfoKHR'
_member_list_ = ['sType', 'pNext', 'waitSemaphoreCount', 'pWaitSemaphores', 'swapchainCount', 'pSwapchains', 'pImageIndices', 'pResults']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PRESENT_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'waitSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pWaitSemaphores': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['waitSemaphoreCount']],
        'is_string': False,
    },
    'swapchainCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSwapchains': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['swapchainCount']],
        'is_string': False,
    },
    'pImageIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['swapchainCount']],
        'is_string': False,
    },
    'pResults': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkResult',
        'enum': 'VkResult',
        'length': [['swapchainCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkDeviceGroupPresentInfoKHR',
    'VkDisplayPresentInfoKHR',
    'VkFrameBoundaryEXT',
    'VkPresentFrameTokenGGP',
    'VkPresentIdKHR',
    'VkPresentRegionsKHR',
    'VkPresentTimesInfoGOOGLE',
    'VkSwapchainPresentFenceInfoEXT',
    'VkSwapchainPresentModeInfoEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkQueuePresentKHR',
}
_output_of_ = set()
