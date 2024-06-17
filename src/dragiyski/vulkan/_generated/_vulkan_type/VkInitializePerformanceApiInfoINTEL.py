import ctypes, sys

class VkInitializePerformanceApiInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pUserData', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkInitializePerformanceApiInfoINTEL
