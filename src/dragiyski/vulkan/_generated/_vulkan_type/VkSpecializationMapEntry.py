import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('constantID', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_size_t),
    ]
