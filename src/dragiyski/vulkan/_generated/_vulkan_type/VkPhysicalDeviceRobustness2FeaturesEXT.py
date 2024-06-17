import ctypes, sys

class VkPhysicalDeviceRobustness2FeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustBufferAccess2', ctypes.c_uint32),
        ('robustImageAccess2', ctypes.c_uint32),
        ('nullDescriptor', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRobustness2FeaturesEXT
