import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentMask', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('modes', ctypes.c_uint32),
    ]
