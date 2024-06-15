import ctypes, sys

class VkSemaphoreSignalInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkSemaphoreSignalInfo
