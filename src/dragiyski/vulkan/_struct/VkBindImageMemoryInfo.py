import ctypes, sys

class VkBindImageMemoryInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkBindImageMemoryInfo
