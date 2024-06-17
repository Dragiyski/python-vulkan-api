import ctypes, sys

class VkQueueFamilyQueryResultStatusPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryResultStatusSupport', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkQueueFamilyQueryResultStatusPropertiesKHR
