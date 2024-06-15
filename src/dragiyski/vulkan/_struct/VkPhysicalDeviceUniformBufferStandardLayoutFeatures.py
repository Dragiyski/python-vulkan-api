import ctypes, sys

class VkPhysicalDeviceUniformBufferStandardLayoutFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('uniformBufferStandardLayout', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceUniformBufferStandardLayoutFeatures
