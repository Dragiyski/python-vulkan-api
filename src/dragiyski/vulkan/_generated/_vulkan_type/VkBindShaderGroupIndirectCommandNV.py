import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('groupIndex', ctypes.c_uint32),
    ]
