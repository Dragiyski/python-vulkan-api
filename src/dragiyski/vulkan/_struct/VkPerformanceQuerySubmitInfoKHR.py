import ctypes, sys

class VkPerformanceQuerySubmitInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('counterPassIndex', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPerformanceQuerySubmitInfoKHR
