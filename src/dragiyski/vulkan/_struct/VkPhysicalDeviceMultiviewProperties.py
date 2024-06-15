import ctypes, sys

class VkPhysicalDeviceMultiviewProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxMultiviewViewCount', ctypes.c_uint32),
        ('maxMultiviewInstanceIndex', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMultiviewProperties
