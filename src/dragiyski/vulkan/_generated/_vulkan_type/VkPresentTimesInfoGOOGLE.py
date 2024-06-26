import ctypes

class VkPresentTimesInfoGOOGLE(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkPresentInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkPresentTimeGOOGLE',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'swapchainCount': 'swapchain_count',
        'pTimes': 'times',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_GOOGLE_display_timing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PRESENT_TIMES_INFO_GOOGLE
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPresentTimeGOOGLE import VkPresentTimeGOOGLE

VkPresentTimesInfoGOOGLE._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('swapchainCount', ctypes.c_uint32),
    ('pTimes', ctypes.POINTER(VkPresentTimeGOOGLE)),
]

VkPresentTimesInfoGOOGLE._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchainCount': ctypes.c_uint32,
    'pTimes': ctypes.POINTER(VkPresentTimeGOOGLE),
}
