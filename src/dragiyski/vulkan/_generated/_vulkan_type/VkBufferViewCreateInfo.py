import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]
