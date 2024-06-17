import ctypes, sys

class VkPipelineViewportShadingRateImageStateCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkPipelineViewportShadingRateImageStateCreateInfoNV

from . import VkShadingRatePaletteNV

VkPipelineViewportShadingRateImageStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateImageEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pShadingRatePalettes', ctypes.POINTER(VkShadingRatePaletteNV)),
]
