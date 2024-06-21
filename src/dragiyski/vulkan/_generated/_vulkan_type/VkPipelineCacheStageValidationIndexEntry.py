import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('codeSize', ctypes.c_uint64),
        ('codeOffset', ctypes.c_uint64),
    ]
