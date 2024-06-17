import ctypes, sys

class VkVideoCodingControlInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkVideoCodingControlInfoKHR
