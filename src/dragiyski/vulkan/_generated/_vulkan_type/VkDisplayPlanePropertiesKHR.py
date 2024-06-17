import ctypes, sys

class VkDisplayPlanePropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('currentDisplay', ctypes.c_void_p),
        ('currentStackIndex', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkDisplayPlanePropertiesKHR
