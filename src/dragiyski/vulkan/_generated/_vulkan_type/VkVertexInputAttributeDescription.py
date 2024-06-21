import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('location', ctypes.c_uint32),
        ('binding', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint32),
    ]
