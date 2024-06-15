import ctypes, sys

class VkPhysicalDeviceFrameBoundaryFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('frameBoundary', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFrameBoundaryFeaturesEXT