import ctypes, sys

class VkPhysicalDeviceVideoFormatInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageUsage', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceVideoFormatInfoKHR
