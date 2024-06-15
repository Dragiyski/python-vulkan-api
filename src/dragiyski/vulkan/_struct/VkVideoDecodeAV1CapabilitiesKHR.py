import ctypes, sys

class VkVideoDecodeAV1CapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxLevel', ctypes.c_int),
    ]

sys.modules[__name__] = VkVideoDecodeAV1CapabilitiesKHR
