import ctypes, sys

class VkPhysicalDeviceRayTracingPositionFetchFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rayTracingPositionFetch', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRayTracingPositionFetchFeaturesKHR
