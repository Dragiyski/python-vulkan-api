import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('textureSampleWeighted', ctypes.c_uint32),
        ('textureBoxFilter', ctypes.c_uint32),
        ('textureBlockMatch', ctypes.c_uint32),
    ]
