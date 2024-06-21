import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]
