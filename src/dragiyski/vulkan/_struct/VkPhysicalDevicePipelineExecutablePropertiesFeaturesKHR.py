import ctypes, sys

class VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineExecutableInfo', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePipelineExecutablePropertiesFeaturesKHR
