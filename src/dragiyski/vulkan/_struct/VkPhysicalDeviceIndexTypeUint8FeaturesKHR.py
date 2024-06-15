import ctypes, sys

class VkPhysicalDeviceIndexTypeUint8FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('indexTypeUint8', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceIndexTypeUint8FeaturesKHR
