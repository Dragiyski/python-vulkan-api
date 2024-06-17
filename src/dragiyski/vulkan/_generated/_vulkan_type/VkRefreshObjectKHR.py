import ctypes, sys

class VkRefreshObjectKHR(ctypes.Structure):
    _fields_ = [
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkRefreshObjectKHR
