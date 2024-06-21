import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('taskCount', ctypes.c_uint32),
        ('firstTask', ctypes.c_uint32),
    ]
