import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('isText', ctypes.c_uint32),
        ('dataSize', ctypes.c_size_t),
        ('pData', ctypes.c_void_p),
    ]
