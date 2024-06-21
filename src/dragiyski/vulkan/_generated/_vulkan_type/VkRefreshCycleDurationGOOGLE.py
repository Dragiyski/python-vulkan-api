import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('refreshDuration', ctypes.c_uint64),
    ]
