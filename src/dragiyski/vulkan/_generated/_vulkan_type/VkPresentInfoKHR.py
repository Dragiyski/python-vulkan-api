import ctypes

class VkPresentInfoKHR(ctypes.Structure):
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

    _init_ = []
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
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'waitSemaphoreCount': 'wait_semaphore_count',
        'pWaitSemaphores': 'wait_semaphores',
        'swapchainCount': 'swapchain_count',
        'pSwapchains': 'swapchains',
        'pImageIndices': 'image_indices',
        'pResults': 'results',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_swapchain',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pResults': 'VkResult',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PRESENT_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPresentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreCount': ctypes.c_uint32,
    'pWaitSemaphores': ctypes.POINTER(ctypes.c_void_p),
    'swapchainCount': ctypes.c_uint32,
    'pSwapchains': ctypes.POINTER(ctypes.c_void_p),
    'pImageIndices': ctypes.POINTER(ctypes.c_uint32),
    'pResults': ctypes.POINTER(ctypes.c_int),
}
