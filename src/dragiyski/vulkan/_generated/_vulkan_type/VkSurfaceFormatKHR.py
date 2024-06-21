import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('format', ctypes.c_int),
        ('colorSpace', ctypes.c_int),
    ]
