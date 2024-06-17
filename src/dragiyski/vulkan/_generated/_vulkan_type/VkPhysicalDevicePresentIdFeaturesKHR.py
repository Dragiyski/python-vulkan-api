import ctypes, sys

class VkPhysicalDevicePresentIdFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentId', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePresentIdFeaturesKHR
