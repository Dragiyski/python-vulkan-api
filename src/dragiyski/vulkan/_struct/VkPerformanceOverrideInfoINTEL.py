import ctypes, sys

class VkPerformanceOverrideInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
        ('enable', ctypes.c_uint32),
        ('parameter', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPerformanceOverrideInfoINTEL
