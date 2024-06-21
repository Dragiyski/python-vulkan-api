import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('ScalingList4x4', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 16), 6)),
        ('ScalingList8x8', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
        ('ScalingList16x16', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 6)),
        ('ScalingList32x32', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_uint8, 64), 2)),
        ('ScalingListDCCoef16x16', ctypes.ARRAY(ctypes.c_uint8, 6)),
        ('ScalingListDCCoef32x32', ctypes.ARRAY(ctypes.c_uint8, 2)),
    ]
