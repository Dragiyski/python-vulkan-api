import ctypes, sys

class VkPhysicalDeviceShaderSubgroupUniformControlFlowFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderSubgroupUniformControlFlow', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceShaderSubgroupUniformControlFlowFeaturesKHR
