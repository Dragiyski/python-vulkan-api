import ctypes, sys

class VkPhysicalDeviceLineRasterizationPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('lineSubPixelPrecisionBits', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceLineRasterizationPropertiesKHR
