import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]
