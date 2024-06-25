import ctypes

class VkRefreshCycleDurationGOOGLE(ctypes.Structure):
    _fields_ = [
        ('refreshDuration', ctypes.c_uint64),
    ]

VkRefreshCycleDurationGOOGLE._type_ = {
    'refreshDuration': ctypes.c_uint64,
}
