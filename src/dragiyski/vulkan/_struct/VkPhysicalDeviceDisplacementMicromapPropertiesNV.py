import ctypes, sys

class VkPhysicalDeviceDisplacementMicromapPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxDisplacementMicromapSubdivisionLevel', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDisplacementMicromapPropertiesNV
