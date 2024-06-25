import ctypes

class VkSurfaceCapabilitiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
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
