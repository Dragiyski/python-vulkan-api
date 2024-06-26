import ctypes

class VkSharedPresentSurfaceCapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sharedPresentSupportedUsageFlags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkSurfaceCapabilities2KHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'sharedPresentSupportedUsageFlags': 'shared_present_supported_usage_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_shared_presentable_image',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'sharedPresentSupportedUsageFlags': 'VkImageUsageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SHARED_PRESENT_SURFACE_CAPABILITIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHARED_PRESENT_SURFACE_CAPABILITIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkSharedPresentSurfaceCapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sharedPresentSupportedUsageFlags': ctypes.c_uint32,
}
