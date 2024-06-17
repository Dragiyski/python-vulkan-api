import ctypes, sys

class VkPhysicalDeviceCubicClampFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cubicRangeClamp', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceCubicClampFeaturesQCOM
