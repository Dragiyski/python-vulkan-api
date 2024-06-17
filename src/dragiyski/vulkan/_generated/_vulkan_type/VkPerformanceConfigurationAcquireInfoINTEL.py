import ctypes, sys

class VkPerformanceConfigurationAcquireInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('type', ctypes.c_int),
    ]

sys.modules[__name__] = VkPerformanceConfigurationAcquireInfoINTEL
