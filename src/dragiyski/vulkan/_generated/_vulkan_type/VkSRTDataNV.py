import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sx', ctypes.c_float),
        ('a', ctypes.c_float),
        ('b', ctypes.c_float),
        ('pvx', ctypes.c_float),
        ('sy', ctypes.c_float),
        ('c', ctypes.c_float),
        ('pvy', ctypes.c_float),
        ('sz', ctypes.c_float),
        ('pvz', ctypes.c_float),
        ('qx', ctypes.c_float),
        ('qy', ctypes.c_float),
        ('qz', ctypes.c_float),
        ('qw', ctypes.c_float),
        ('tx', ctypes.c_float),
        ('ty', ctypes.c_float),
        ('tz', ctypes.c_float),
    ]
