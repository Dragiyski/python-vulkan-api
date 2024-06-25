import ctypes

class VkSurfacePresentScalingCapabilitiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'supportedPresentScaling': ctypes.c_uint32,
            'supportedPresentGravityX': ctypes.c_uint32,
            'supportedPresentGravityY': ctypes.c_uint32,
            'minScaledImageExtent': VkExtent2D,
            'maxScaledImageExtent': VkExtent2D,
        }


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
