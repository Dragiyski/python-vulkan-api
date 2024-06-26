import ctypes

class VkSurfacePresentScalingCapabilitiesEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkSurfaceCapabilities2KHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'supportedPresentScaling': 'supported_present_scaling',
        'supportedPresentGravityX': 'supported_present_gravity_x',
        'supportedPresentGravityY': 'supported_present_gravity_y',
        'minScaledImageExtent': 'min_scaled_image_extent',
        'maxScaledImageExtent': 'max_scaled_image_extent',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_surface_maintenance1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'supportedPresentScaling': 'VkPresentScalingFlagsEXT',
        'supportedPresentGravityX': 'VkPresentGravityFlagsEXT',
        'supportedPresentGravityY': 'VkPresentGravityFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SURFACE_PRESENT_SCALING_CAPABILITIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_PRESENT_SCALING_CAPABILITIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkSurfacePresentScalingCapabilitiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('supportedPresentScaling', ctypes.c_uint32),
    ('supportedPresentGravityX', ctypes.c_uint32),
    ('supportedPresentGravityY', ctypes.c_uint32),
    ('minScaledImageExtent', VkExtent2D),
    ('maxScaledImageExtent', VkExtent2D),
]

VkSurfacePresentScalingCapabilitiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportedPresentScaling': ctypes.c_uint32,
    'supportedPresentGravityX': ctypes.c_uint32,
    'supportedPresentGravityY': ctypes.c_uint32,
    'minScaledImageExtent': VkExtent2D,
    'maxScaledImageExtent': VkExtent2D,
}
