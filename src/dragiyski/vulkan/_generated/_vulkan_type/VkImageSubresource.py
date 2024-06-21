import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('arrayLayer', ctypes.c_uint32),
    ]
