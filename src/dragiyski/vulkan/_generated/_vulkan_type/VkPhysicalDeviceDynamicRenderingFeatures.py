import ctypes, sys

class VkPhysicalDeviceDynamicRenderingFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dynamicRendering', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDynamicRenderingFeatures
