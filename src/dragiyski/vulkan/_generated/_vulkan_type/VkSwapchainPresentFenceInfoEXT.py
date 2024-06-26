import ctypes

class VkSwapchainPresentFenceInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainCount', ctypes.c_uint32),
        ('pFences', ctypes.POINTER(ctypes.c_void_p)),
    ]

    _init_ = []
    _extends_ = {
        'VkPresentInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'swapchainCount': 'swapchain_count',
        'pFences': 'fences',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_swapchain_maintenance1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_FENCE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_PRESENT_FENCE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkSwapchainPresentFenceInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'swapchainCount': ctypes.c_uint32,
    'pFences': ctypes.POINTER(ctypes.c_void_p),
}
