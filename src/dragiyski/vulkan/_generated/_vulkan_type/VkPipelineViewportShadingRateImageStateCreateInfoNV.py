import ctypes

class VkPipelineViewportShadingRateImageStateCreateInfoNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shadingRateImageEnable': ctypes.c_uint32,
            'viewportCount': ctypes.c_uint32,
            'pShadingRatePalettes': ctypes.POINTER(VkShadingRatePaletteNV),
        }


from .VkShadingRatePaletteNV import VkShadingRatePaletteNV

VkPipelineViewportShadingRateImageStateCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateImageEnable', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pShadingRatePalettes', ctypes.POINTER(VkShadingRatePaletteNV)),
]
