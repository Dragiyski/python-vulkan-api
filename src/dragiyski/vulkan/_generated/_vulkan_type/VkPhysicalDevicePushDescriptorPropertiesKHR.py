import ctypes, sys

class VkPhysicalDevicePushDescriptorPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPushDescriptors', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePushDescriptorPropertiesKHR
