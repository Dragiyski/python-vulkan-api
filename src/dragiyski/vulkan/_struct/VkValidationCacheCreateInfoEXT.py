import ctypes, sys

class VkValidationCacheCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('initialDataSize', ctypes.c_size_t),
        ('pInitialData', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkValidationCacheCreateInfoEXT
