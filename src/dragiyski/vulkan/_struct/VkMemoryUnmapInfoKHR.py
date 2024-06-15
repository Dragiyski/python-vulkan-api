import ctypes, sys

class VkMemoryUnmapInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('memory', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkMemoryUnmapInfoKHR
