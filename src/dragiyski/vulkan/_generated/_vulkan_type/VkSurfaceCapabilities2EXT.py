import ctypes

class VkSurfaceCapabilities2EXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceSurfaceCapabilities2EXT',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'minImageCount': 'min_image_count',
        'maxImageCount': 'max_image_count',
        'currentExtent': 'current_extent',
        'minImageExtent': 'min_image_extent',
        'maxImageExtent': 'max_image_extent',
        'maxImageArrayLayers': 'max_image_array_layers',
        'supportedTransforms': 'supported_transforms',
        'currentTransform': 'current_transform',
        'supportedCompositeAlpha': 'supported_composite_alpha',
        'supportedUsageFlags': 'supported_usage_flags',
        'supportedSurfaceCounters': 'supported_surface_counters',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_display_surface_counter',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'supportedTransforms': 'VkSurfaceTransformFlagsKHR',
        'supportedCompositeAlpha': 'VkCompositeAlphaFlagsKHR',
        'supportedUsageFlags': 'VkImageUsageFlags',
        'supportedSurfaceCounters': 'VkSurfaceCounterFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SURFACE_CAPABILITIES_2_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkSurfaceCapabilities2EXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('minImageCount', ctypes.c_uint32),
    ('maxImageCount', ctypes.c_uint32),
    ('currentExtent', VkExtent2D),
    ('minImageExtent', VkExtent2D),
    ('maxImageExtent', VkExtent2D),
    ('maxImageArrayLayers', ctypes.c_uint32),
    ('supportedTransforms', ctypes.c_uint32),
    ('currentTransform', ctypes.c_uint32),
    ('supportedCompositeAlpha', ctypes.c_uint32),
    ('supportedUsageFlags', ctypes.c_uint32),
    ('supportedSurfaceCounters', ctypes.c_uint32),
]

VkSurfaceCapabilities2EXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'minImageCount': ctypes.c_uint32,
    'maxImageCount': ctypes.c_uint32,
    'currentExtent': VkExtent2D,
    'minImageExtent': VkExtent2D,
    'maxImageExtent': VkExtent2D,
    'maxImageArrayLayers': ctypes.c_uint32,
    'supportedTransforms': ctypes.c_uint32,
    'currentTransform': ctypes.c_uint32,
    'supportedCompositeAlpha': ctypes.c_uint32,
    'supportedUsageFlags': ctypes.c_uint32,
    'supportedSurfaceCounters': ctypes.c_uint32,
}
