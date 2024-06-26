import ctypes

class VkSurfaceCapabilitiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = {
        'VkSurfaceCapabilities2KHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceSurfaceCapabilitiesKHR',
    }
    _python_name_ = {
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
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_surface',
    }
    _vk_enum_ = {
        'supportedTransforms': 'VkSurfaceTransformFlagsKHR',
        'supportedCompositeAlpha': 'VkCompositeAlphaFlagsKHR',
        'supportedUsageFlags': 'VkImageUsageFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkSurfaceCapabilitiesKHR._fields_ = [
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
]

VkSurfaceCapabilitiesKHR._type_ = {
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
}
