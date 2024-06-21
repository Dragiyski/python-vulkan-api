import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('clientType', ctypes.c_int),
        ('primitiveType', ctypes.c_int),
    ]