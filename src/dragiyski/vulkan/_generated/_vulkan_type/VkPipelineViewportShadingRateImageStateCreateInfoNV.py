import ctypes

class VkPipelineViewportShadingRateImageStateCreateInfoNV(ctypes.Structure):
    pass

from .VkShadingRatePaletteNV import VkShadingRatePaletteNV

VkPipelineViewportShadingRateImageStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateImageEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pShadingRatePalettes', ctypes.POINTER(VkShadingRatePaletteNV)),
]

VkPipelineViewportShadingRateImageStateCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'shadingRateImageEnable': ctypes.c_uint32,
    'viewportCount': ctypes.c_uint32,
    'pShadingRatePalettes': ctypes.POINTER(VkShadingRatePaletteNV),
}
