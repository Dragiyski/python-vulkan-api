import ctypes, sys

class VkPerformanceStreamMarkerInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('marker', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPerformanceStreamMarkerInfoINTEL
