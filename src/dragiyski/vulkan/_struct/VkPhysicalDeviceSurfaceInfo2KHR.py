import ctypes, sys

class VkPhysicalDeviceSurfaceInfo2KHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkPhysicalDeviceSurfaceInfo2KHR
