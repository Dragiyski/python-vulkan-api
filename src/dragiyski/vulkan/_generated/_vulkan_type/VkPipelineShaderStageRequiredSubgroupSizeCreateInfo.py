import ctypes

class VkPipelineShaderStageRequiredSubgroupSizeCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('requiredSubgroupSize', ctypes.c_uint32),
    ]

VkPipelineShaderStageRequiredSubgroupSizeCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'requiredSubgroupSize': ctypes.c_uint32,
}
