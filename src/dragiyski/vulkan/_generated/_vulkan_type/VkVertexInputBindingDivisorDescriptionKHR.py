import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('divisor', ctypes.c_uint32),
    ]
