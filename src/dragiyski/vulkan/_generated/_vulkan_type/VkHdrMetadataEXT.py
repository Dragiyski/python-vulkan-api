import ctypes

class CType(ctypes.Structure):
    pass

from .VkXYColorEXT import CType as VkXYColorEXT

CType._fields_ = [
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
