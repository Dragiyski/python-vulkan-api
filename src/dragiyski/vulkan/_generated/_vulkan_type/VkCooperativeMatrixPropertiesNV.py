import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('MSize', ctypes.c_uint32),
        ('NSize', ctypes.c_uint32),
        ('KSize', ctypes.c_uint32),
        ('AType', ctypes.c_int),
        ('BType', ctypes.c_int),
        ('CType', ctypes.c_int),
        ('DType', ctypes.c_int),
        ('scope', ctypes.c_int),
    ]
