import ctypes, sys

class VkMemoryFdPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryFdPropertiesKHR
