import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('pObjectName', ctypes.c_char_p),
    ]
