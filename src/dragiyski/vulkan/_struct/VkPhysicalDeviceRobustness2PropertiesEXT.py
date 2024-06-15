import ctypes, sys

class VkPhysicalDeviceRobustness2PropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustStorageBufferAccessSizeAlignment', ctypes.c_uint64),
        ('robustUniformBufferAccessSizeAlignment', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkPhysicalDeviceRobustness2PropertiesEXT
