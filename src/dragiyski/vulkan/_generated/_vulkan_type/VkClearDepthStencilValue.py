import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('depth', ctypes.c_float),
        ('stencil', ctypes.c_uint32),
    ]
