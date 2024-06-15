import ctypes, sys

class VkPhysicalDeviceTexelBufferAlignmentFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('texelBufferAlignment', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceTexelBufferAlignmentFeaturesEXT
