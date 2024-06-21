import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('dataOffset', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint16),
        ('format', ctypes.c_uint16),
    ]
