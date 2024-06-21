import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
    ]
