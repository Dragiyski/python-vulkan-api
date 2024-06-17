import ctypes, sys

class VkPhysicalDeviceDedicatedAllocationImageAliasingFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dedicatedAllocationImageAliasing', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDedicatedAllocationImageAliasingFeaturesNV
