import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterCubic', ctypes.c_uint32),
        ('filterCubicMinmax', ctypes.c_uint32),
    ]
