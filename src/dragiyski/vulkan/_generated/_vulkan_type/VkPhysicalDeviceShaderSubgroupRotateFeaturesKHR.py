import ctypes, sys

class VkPhysicalDeviceShaderSubgroupRotateFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSubgroupRotate', ctypes.c_uint32),
        ('shaderSubgroupRotateClustered', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderSubgroupRotateFeaturesKHR
