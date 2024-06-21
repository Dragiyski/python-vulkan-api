import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderBufferInt64Atomics', ctypes.c_uint32),
        ('shaderSharedInt64Atomics', ctypes.c_uint32),
    ]
