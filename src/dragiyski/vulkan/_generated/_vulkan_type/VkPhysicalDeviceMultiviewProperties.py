import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxMultiviewViewCount', ctypes.c_uint32),
        ('maxMultiviewInstanceIndex', ctypes.c_uint32),
    ]
