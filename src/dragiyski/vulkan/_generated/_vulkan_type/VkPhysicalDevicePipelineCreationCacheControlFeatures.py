import ctypes, sys

class VkPhysicalDevicePipelineCreationCacheControlFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineCreationCacheControl', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePipelineCreationCacheControlFeatures
