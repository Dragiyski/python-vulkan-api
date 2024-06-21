import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
    ]
