import ctypes, sys

class VkMemoryBarrier(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcAccessMask', ctypes.c_uint32),
        ('dstAccessMask', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkMemoryBarrier
