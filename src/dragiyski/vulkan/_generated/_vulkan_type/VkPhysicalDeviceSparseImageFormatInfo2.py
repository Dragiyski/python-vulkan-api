import ctypes, sys

class VkPhysicalDeviceSparseImageFormatInfo2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('type', ctypes.c_int),
        ('samples', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('tiling', ctypes.c_int),
    ]

sys.modules[__name__] = VkPhysicalDeviceSparseImageFormatInfo2
