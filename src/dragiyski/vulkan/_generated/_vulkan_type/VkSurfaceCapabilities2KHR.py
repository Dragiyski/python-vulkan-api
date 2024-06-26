import ctypes

class VkSurfaceCapabilities2KHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDisplayNativeHdrSurfaceCapabilitiesAMD',
        'VkLatencySurfaceCapabilitiesNV',
        'VkSharedPresentSurfaceCapabilitiesKHR',
        'VkSurfaceCapabilitiesFullScreenExclusiveEXT',
        'VkSurfaceCapabilitiesPresentBarrierNV',
        'VkSurfacePresentModeCompatibilityEXT',
        'VkSurfacePresentScalingCapabilitiesEXT',
        'VkSurfaceProtectedCapabilitiesKHR',
    }
    _includes_ = {
        'VkSurfaceCapabilitiesKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'surfaceCapabilities': 'surface_capabilities',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_get_surface_capabilities2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSurfaceCapabilitiesKHR import VkSurfaceCapabilitiesKHR

VkSurfaceCapabilities2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceCapabilities', VkSurfaceCapabilitiesKHR),
]

VkSurfaceCapabilities2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'surfaceCapabilities': VkSurfaceCapabilitiesKHR,
}
