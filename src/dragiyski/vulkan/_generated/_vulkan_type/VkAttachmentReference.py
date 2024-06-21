import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
    ]
