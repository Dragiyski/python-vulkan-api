import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('matrix', ctypes.ARRAY(ctypes.ARRAY(ctypes.c_float, 4), 3)),
    ]
