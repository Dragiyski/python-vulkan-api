import ctypes

class VkSurfaceCapabilities2EXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
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
