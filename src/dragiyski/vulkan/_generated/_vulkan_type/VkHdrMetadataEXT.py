import ctypes, sys

class VkHdrMetadataEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkHdrMetadataEXT

from . import VkXYColorEXT

VkHdrMetadataEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPrimaryRed', VkXYColorEXT),
    ('displayPrimaryGreen', VkXYColorEXT),
    ('displayPrimaryBlue', VkXYColorEXT),
    ('whitePoint', VkXYColorEXT),
    ('maxLuminance', ctypes.c_float),
    ('minLuminance', ctypes.c_float),
    ('maxContentLightLevel', ctypes.c_float),
    ('maxFrameAverageLightLevel', ctypes.c_float),
]
