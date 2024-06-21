import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('flags', ctypes.c_uint32),
        ('duration', ctypes.c_uint64),
    ]
