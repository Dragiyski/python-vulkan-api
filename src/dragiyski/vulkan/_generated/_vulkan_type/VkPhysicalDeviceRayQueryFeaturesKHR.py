import ctypes, sys

class VkPhysicalDeviceRayQueryFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayQuery', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRayQueryFeaturesKHR
