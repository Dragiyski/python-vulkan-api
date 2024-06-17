import ctypes, sys

class VkVideoDecodeUsageInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoUsageHints', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoDecodeUsageInfoKHR
