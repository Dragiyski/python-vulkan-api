import ctypes, sys

class VkPhysicalDeviceYcbcr2Plane444FormatsFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('ycbcr2plane444Formats', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceYcbcr2Plane444FormatsFeaturesEXT
