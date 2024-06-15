import ctypes, sys

class VkSemaphoreTypeCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphoreType', ctypes.c_int),
        ('initialValue', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkSemaphoreTypeCreateInfo
