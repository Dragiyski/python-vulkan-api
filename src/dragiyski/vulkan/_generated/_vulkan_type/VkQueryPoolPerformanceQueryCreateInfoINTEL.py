import ctypes, sys

class VkQueryPoolPerformanceQueryCreateInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('performanceCountersSampling', ctypes.c_int),
    ]

sys.modules[__name__] = VkQueryPoolPerformanceQueryCreateInfoINTEL
