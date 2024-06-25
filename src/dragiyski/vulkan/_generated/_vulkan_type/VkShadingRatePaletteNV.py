import ctypes

class VkShadingRatePaletteNV(ctypes.Structure):
    _fields_ = [
        ('shadingRatePaletteEntryCount', ctypes.c_uint32),
        ('pShadingRatePaletteEntries', ctypes.POINTER(ctypes.c_int)),
    ]

VkShadingRatePaletteNV._type_ = {
    'shadingRatePaletteEntryCount': ctypes.c_uint32,
    'pShadingRatePaletteEntries': ctypes.POINTER(ctypes.c_int),
}
