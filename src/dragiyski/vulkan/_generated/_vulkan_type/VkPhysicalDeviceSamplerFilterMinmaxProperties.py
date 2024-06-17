import ctypes, sys

class VkPhysicalDeviceSamplerFilterMinmaxProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterMinmaxSingleComponentFormats', ctypes.c_uint32),
        ('filterMinmaxImageComponentMapping', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceSamplerFilterMinmaxProperties
