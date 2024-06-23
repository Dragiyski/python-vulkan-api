import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreCount', ctypes.c_uint32),
        ('pWaitSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('swapchainCount', ctypes.c_uint32),
        ('pSwapchains', ctypes.POINTER(ctypes.c_void_p)),
        ('pImageIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pResults', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceGroupPresentInfoKHR',
        'VkDisplayPresentInfoKHR',
        'VkFrameBoundaryEXT',
        'VkPresentFrameTokenGGP',
        'VkPresentIdKHR',
        'VkPresentRegionsKHR',
        'VkPresentTimesInfoGOOGLE',
        'VkSwapchainPresentFenceInfoEXT',
        'VkSwapchainPresentModeInfoEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkQueuePresentKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PRESENT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'waitSemaphoreCount': {'python_name': ['wait', 'semaphore', 'count']},
        'pWaitSemaphores': {'python_name': ['p', 'wait', 'semaphores'], 'len': [['waitSemaphoreCount']]},
        'swapchainCount': {'python_name': ['swapchain', 'count']},
        'pSwapchains': {'python_name': ['p', 'swapchains'], 'len': [['swapchainCount']]},
        'pImageIndices': {'python_name': ['p', 'image', 'indices'], 'len': [['swapchainCount']]},
        'pResults': {'python_name': ['p', 'results'], 'len': [['swapchainCount']], 'type': 'VkResult'},
    }
}
