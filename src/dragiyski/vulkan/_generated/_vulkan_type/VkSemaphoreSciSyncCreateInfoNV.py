import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphorePool', ctypes.c_void_p),
        ('pFence', ctypes.POINTER(ctypes.ARRAY(ctypes.c_uint64, 6))),
    ]
