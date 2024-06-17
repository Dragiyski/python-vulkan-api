import ctypes, sys

class VkMemoryAllocateFlagsInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('deviceMask', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryAllocateFlagsInfo
