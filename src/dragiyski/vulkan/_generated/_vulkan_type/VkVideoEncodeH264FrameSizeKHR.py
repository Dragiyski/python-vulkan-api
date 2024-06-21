import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('frameISize', ctypes.c_uint32),
        ('framePSize', ctypes.c_uint32),
        ('frameBSize', ctypes.c_uint32),
    ]
