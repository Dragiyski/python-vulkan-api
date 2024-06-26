import ctypes

class VkSwapchainDisplayNativeHdrCreateInfoAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('localDimmingEnable', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkSwapchainCreateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'localDimmingEnable': 'local_dimming_enable',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_display_native_hdr',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SWAPCHAIN_DISPLAY_NATIVE_HDR_CREATE_INFO_AMD'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SWAPCHAIN_DISPLAY_NATIVE_HDR_CREATE_INFO_AMD
        for function in self._init_:
            function(self, *args, **kwargs)

VkSwapchainDisplayNativeHdrCreateInfoAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'localDimmingEnable': ctypes.c_uint32,
}
