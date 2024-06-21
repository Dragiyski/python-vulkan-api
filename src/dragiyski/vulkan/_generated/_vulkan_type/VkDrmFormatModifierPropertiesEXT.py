import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('drmFormatModifier', ctypes.c_uint64),
        ('drmFormatModifierPlaneCount', ctypes.c_uint32),
        ('drmFormatModifierTilingFeatures', ctypes.c_uint32),
    ]
