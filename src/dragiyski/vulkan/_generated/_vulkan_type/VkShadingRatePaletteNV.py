import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('shadingRatePaletteEntryCount', ctypes.c_uint32),
        ('pShadingRatePaletteEntries', ctypes.POINTER(ctypes.c_int)),
    ]
