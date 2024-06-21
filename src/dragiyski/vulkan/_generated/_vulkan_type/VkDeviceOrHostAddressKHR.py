import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]
