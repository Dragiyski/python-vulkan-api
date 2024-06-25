import ctypes

class VkRefreshObjectKHR(ctypes.Structure):
    _fields_ = [
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

VkRefreshObjectKHR._type_ = {
    'objectType': ctypes.c_int,
    'objectHandle': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
