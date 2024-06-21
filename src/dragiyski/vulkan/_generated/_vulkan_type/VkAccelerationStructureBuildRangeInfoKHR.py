import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('primitiveCount', ctypes.c_uint32),
        ('primitiveOffset', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('transformOffset', ctypes.c_uint32),
    ]
