import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('semaphoreCount', ctypes.c_uint32),
        ('pSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('pValues', ctypes.POINTER(ctypes.c_uint64)),
    ]
