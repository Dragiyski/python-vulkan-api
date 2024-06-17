import ctypes, sys

class VkPhysicalDevicePipelineRobustnessFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineRobustness', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevicePipelineRobustnessFeaturesEXT
