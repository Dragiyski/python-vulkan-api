import ctypes, sys

class VkPipelineShaderStageRequiredSubgroupSizeCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('requiredSubgroupSize', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPipelineShaderStageRequiredSubgroupSizeCreateInfo
