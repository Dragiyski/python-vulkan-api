import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('vertexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('firstInstance', ctypes.c_uint32),
    ]
