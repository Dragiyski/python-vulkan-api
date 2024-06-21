import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('b32', ctypes.c_uint32),
        ('i64', ctypes.c_int64),
        ('u64', ctypes.c_uint64),
        ('f64', ctypes.c_double),
    ]
