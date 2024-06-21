import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSMCount', ctypes.c_uint32),
        ('shaderWarpsPerSM', ctypes.c_uint32),
    ]
