import ctypes, sys

class VkPhysicalDevicePipelineProtectedAccessFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineProtectedAccess', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePipelineProtectedAccessFeaturesEXT
