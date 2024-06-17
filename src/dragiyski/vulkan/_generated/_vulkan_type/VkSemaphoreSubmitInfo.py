import ctypes, sys

class VkSemaphoreSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
        ('stageMask', ctypes.c_uint64),
        ('deviceIndex', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSemaphoreSubmitInfo
