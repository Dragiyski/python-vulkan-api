import ctypes, sys

class VkPhysicalDeviceNestedCommandBufferPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxCommandBufferNestingLevel', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceNestedCommandBufferPropertiesEXT
