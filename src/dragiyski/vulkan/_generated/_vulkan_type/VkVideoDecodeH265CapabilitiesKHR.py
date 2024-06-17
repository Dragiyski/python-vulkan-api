import ctypes, sys

class VkVideoDecodeH265CapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxLevelIdc', ctypes.c_int),
    ]

sys.modules[__name__] = VkVideoDecodeH265CapabilitiesKHR
