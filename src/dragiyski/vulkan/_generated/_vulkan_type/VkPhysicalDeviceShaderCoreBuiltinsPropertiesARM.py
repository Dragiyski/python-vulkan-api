import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreMask', ctypes.c_uint64),
        ('shaderCoreCount', ctypes.c_uint32),
        ('shaderWarpsPerCore', ctypes.c_uint32),
    ]
