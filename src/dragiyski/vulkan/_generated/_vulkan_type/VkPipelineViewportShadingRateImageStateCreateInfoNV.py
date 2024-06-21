import ctypes

class CType(ctypes.Structure):
    pass

from .VkShadingRatePaletteNV import CType as VkShadingRatePaletteNV

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateImageEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pShadingRatePalettes', ctypes.POINTER(VkShadingRatePaletteNV)),
]
