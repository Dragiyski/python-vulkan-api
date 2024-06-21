import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('timeout', ctypes.c_uint64),
        ('semaphore', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]
