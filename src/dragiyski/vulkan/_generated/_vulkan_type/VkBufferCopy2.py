import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcOffset', ctypes.c_uint64),
        ('dstOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]
