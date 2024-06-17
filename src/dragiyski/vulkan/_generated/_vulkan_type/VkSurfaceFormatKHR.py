import ctypes, sys

class VkSurfaceFormatKHR(ctypes.Structure):
    _fields_ = [
        ('format', ctypes.c_int),
        ('colorSpace', ctypes.c_int),
    ]

sys.modules[__name__] = VkSurfaceFormatKHR
