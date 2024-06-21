import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
    ]
