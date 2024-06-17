import ctypes, sys

class VkQueueFamilyVideoPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoCodecOperations', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkQueueFamilyVideoPropertiesKHR
