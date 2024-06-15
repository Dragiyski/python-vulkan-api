import ctypes, sys

class VkMemoryWin32HandlePropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryWin32HandlePropertiesKHR
