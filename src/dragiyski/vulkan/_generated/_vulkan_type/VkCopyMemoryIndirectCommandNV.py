import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]
