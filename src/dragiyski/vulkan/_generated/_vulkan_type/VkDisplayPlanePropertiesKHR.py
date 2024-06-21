import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('currentDisplay', ctypes.c_void_p),
        ('currentStackIndex', ctypes.c_uint32),
    ]
