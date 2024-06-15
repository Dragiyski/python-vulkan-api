import ctypes, sys

class VkSwapchainCounterCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('surfaceCounters', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSwapchainCounterCreateInfoEXT
