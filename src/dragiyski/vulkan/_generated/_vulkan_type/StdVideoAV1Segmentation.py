import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('FeatureEnabled', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('FeatureData', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int16, 8), 8)),
    ]
