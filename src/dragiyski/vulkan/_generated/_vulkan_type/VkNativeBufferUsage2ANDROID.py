import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('consumer', ctypes.c_uint64),
        ('producer', ctypes.c_uint64),
    ]
