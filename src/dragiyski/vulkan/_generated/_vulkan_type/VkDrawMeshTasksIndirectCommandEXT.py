import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('groupCountX', ctypes.c_uint32),
        ('groupCountY', ctypes.c_uint32),
        ('groupCountZ', ctypes.c_uint32),
    ]
