import ctypes, sys

class VkComputePipelineCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkComputePipelineCreateInfo

from . import VkPipelineShaderStageCreateInfo

VkComputePipelineCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', VkPipelineShaderStageCreateInfo),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]
