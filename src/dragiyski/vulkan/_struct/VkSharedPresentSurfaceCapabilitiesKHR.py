import ctypes, sys

class VkSharedPresentSurfaceCapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sharedPresentSupportedUsageFlags', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkSharedPresentSurfaceCapabilitiesKHR
