import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('pixelX', ctypes.c_uint32),
        ('pixelY', ctypes.c_uint32),
        ('sample', ctypes.c_uint32),
    ]
