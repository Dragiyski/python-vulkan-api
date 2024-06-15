import ctypes, sys

class VkPhysicalDeviceLegacyDitheringFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('legacyDithering', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceLegacyDitheringFeaturesEXT
