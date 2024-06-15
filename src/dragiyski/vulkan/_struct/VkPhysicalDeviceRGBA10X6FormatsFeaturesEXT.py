import ctypes, sys

class VkPhysicalDeviceRGBA10X6FormatsFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('formatRgba10x6WithoutYCbCrSampler', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRGBA10X6FormatsFeaturesEXT
