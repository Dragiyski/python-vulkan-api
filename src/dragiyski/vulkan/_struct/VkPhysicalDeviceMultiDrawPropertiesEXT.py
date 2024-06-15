import ctypes, sys

class VkPhysicalDeviceMultiDrawPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxMultiDrawCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMultiDrawPropertiesEXT
