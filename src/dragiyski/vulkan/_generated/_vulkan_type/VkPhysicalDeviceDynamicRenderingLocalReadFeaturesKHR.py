import ctypes, sys

class VkPhysicalDeviceDynamicRenderingLocalReadFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dynamicRenderingLocalRead', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDynamicRenderingLocalReadFeaturesKHR
