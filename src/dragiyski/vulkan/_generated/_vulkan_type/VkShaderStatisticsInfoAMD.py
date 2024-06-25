import ctypes

class VkShaderStatisticsInfoAMD(ctypes.Structure):
    pass

from .VkShaderResourceUsageAMD import VkShaderResourceUsageAMD

VkShaderStatisticsInfoAMD._fields_ = [
    ('shaderStageMask', ctypes.c_uint32),
    ('resourceUsage', VkShaderResourceUsageAMD),
    ('numPhysicalVgprs', ctypes.c_uint32),
    ('numPhysicalSgprs', ctypes.c_uint32),
    ('numAvailableVgprs', ctypes.c_uint32),
    ('numAvailableSgprs', ctypes.c_uint32),
    ('computeWorkGroupSize', ctypes.ARRAY(ctypes.c_uint32, 3)),
]

VkShaderStatisticsInfoAMD._type_ = {
    'shaderStageMask': ctypes.c_uint32,
    'resourceUsage': VkShaderResourceUsageAMD,
    'numPhysicalVgprs': ctypes.c_uint32,
    'numPhysicalSgprs': ctypes.c_uint32,
    'numAvailableVgprs': ctypes.c_uint32,
    'numAvailableSgprs': ctypes.c_uint32,
    'computeWorkGroupSize': ctypes.ARRAY(ctypes.c_uint32, 3),
}
