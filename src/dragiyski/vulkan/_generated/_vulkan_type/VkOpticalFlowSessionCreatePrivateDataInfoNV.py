import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('id', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('pPrivateData', ctypes.c_void_p),
    ]
