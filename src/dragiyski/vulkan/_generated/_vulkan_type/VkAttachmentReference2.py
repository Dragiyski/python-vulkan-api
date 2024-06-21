import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
        ('aspectMask', ctypes.c_uint32),
    ]
