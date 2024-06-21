import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderImageInt64Atomics', ctypes.c_uint32),
        ('sparseImageInt64Atomics', ctypes.c_uint32),
    ]
