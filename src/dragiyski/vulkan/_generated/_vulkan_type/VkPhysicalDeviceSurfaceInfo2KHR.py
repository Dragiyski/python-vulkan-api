import ctypes

class VkPhysicalDeviceSurfaceInfo2KHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkSurfaceFullScreenExclusiveInfoEXT',
        'VkSurfaceFullScreenExclusiveWin32InfoEXT',
        'VkSurfacePresentModeEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetDeviceGroupSurfacePresentModes2EXT',
        'vkGetPhysicalDeviceSurfaceCapabilities2KHR',
        'vkGetPhysicalDeviceSurfaceFormats2KHR',
        'vkGetPhysicalDeviceSurfacePresentModes2EXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'surface': 'surface',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_get_surface_capabilities2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SURFACE_INFO_2_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SURFACE_INFO_2_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceSurfaceInfo2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'surface': ctypes.c_void_p,
}
