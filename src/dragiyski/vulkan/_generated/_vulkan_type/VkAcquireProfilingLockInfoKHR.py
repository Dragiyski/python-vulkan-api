import ctypes, sys

class VkAcquireProfilingLockInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('timeout', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkAcquireProfilingLockInfoKHR
