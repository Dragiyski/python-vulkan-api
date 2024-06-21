import ctypes

class CType(ctypes.Structure):
    pass

from .VkShaderResourceUsageAMD import CType as VkShaderResourceUsageAMD

CType._fields_ = [
    ('shaderStageMask', ctypes.c_uint32),
    ('resourceUsage', VkShaderResourceUsageAMD),
    ('numPhysicalVgprs', ctypes.c_uint32),
    ('numPhysicalSgprs', ctypes.c_uint32),
    ('numAvailableVgprs', ctypes.c_uint32),
    ('numAvailableSgprs', ctypes.c_uint32),
    ('computeWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
]
