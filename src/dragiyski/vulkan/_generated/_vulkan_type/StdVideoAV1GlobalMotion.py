import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('GmType', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('gm_params', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_int32, 6), 8)),
    ]
