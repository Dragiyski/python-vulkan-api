import ctypes, sys

class VkPerformanceCounterDescriptionKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('category', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

sys.modules[__name__] = VkPerformanceCounterDescriptionKHR
