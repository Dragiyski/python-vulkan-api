import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('firstIndex', ctypes.c_uint32),
        ('indexCount', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
    ]
