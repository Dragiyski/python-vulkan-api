import ctypes, sys

class VkMemoryMapInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('memory', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkMemoryMapInfoKHR
