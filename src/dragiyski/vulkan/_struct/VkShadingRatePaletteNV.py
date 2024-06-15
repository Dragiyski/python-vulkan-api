import ctypes, sys

class VkShadingRatePaletteNV(ctypes.Structure):
    _fields_ = [
        ('shadingRatePaletteEntryCount', ctypes.c_uint32),
        ('pShadingRatePaletteEntries', ctypes.POINTER(ctypes.c_int)),
    ]

sys.modules[__name__] = VkShadingRatePaletteNV
