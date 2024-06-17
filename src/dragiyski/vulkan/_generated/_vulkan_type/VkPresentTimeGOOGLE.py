import ctypes, sys

class VkPresentTimeGOOGLE(ctypes.Structure):
    _fields_ = [
        ('presentID', ctypes.c_uint32),
        ('desiredPresentTime', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPresentTimeGOOGLE
