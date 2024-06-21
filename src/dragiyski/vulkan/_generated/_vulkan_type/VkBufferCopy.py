import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcOffset', ctypes.c_uint64),
        ('dstOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]
