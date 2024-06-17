import ctypes, sys

class VkPhysicalDeviceImageFormatInfo2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('type', ctypes.c_int),
        ('tiling', ctypes.c_int),
        ('usage', ctypes.c_uint32),
        ('flags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceImageFormatInfo2
