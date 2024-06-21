import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('data', ctypes.c_uint32),
    ]
