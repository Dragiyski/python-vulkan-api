import ctypes, sys

class VkRefreshCycleDurationGOOGLE(ctypes.Structure):
    _fields_ = [
        ('refreshDuration', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkRefreshCycleDurationGOOGLE
