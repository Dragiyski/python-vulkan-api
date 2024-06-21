import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
    ]
