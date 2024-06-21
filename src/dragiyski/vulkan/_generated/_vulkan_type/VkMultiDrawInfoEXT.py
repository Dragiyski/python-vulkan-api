import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('firstVertex', ctypes.c_uint32),
        ('vertexCount', ctypes.c_uint32),
    ]
