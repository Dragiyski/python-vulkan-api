import ctypes, sys

class VkSurfacePresentScalingCapabilitiesEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkSurfacePresentScalingCapabilitiesEXT

from . import VkExtent2D

VkSurfacePresentScalingCapabilitiesEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('supportedPresentScaling', ctypes.c_uint32),
    ('supportedPresentGravityX', ctypes.c_uint32),
    ('supportedPresentGravityY', ctypes.c_uint32),
    ('minScaledImageExtent', VkExtent2D),
    ('maxScaledImageExtent', VkExtent2D),
]
