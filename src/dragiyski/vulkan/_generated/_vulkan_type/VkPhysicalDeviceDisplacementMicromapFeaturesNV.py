import ctypes, sys

class VkPhysicalDeviceDisplacementMicromapFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('displacementMicromap', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDisplacementMicromapFeaturesNV
