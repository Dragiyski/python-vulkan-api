import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
        ('actualPresentTime', ctypes.c_uint64),
        ('earliestPresentTime', ctypes.c_uint64),
        ('presentMargin', ctypes.c_uint64),
    ]