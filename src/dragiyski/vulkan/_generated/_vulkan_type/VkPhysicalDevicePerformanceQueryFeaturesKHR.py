import ctypes, sys

class VkPhysicalDevicePerformanceQueryFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('performanceCounterQueryPools', ctypes.c_uint32),
        ('performanceCounterMultipleQueryPools', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePerformanceQueryFeaturesKHR
