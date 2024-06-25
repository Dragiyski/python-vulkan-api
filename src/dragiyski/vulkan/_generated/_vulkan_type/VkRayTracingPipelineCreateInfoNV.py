import ctypes

class VkRayTracingPipelineCreateInfoNV(ctypes.Structure):
    pass

from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo
from .VkRayTracingShaderGroupCreateInfoNV import VkRayTracingShaderGroupCreateInfoNV

VkRayTracingPipelineCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkRayTracingShaderGroupCreateInfoNV)),
    ('maxRecursionDepth', ctypes.c_uint32),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

VkRayTracingPipelineCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stageCount': ctypes.c_uint32,
    'pStages': ctypes.POINTER(VkPipelineShaderStageCreateInfo),
    'groupCount': ctypes.c_uint32,
    'pGroups': ctypes.POINTER(VkRayTracingShaderGroupCreateInfoNV),
    'maxRecursionDepth': ctypes.c_uint32,
    'layout': ctypes.c_void_p,
    'basePipelineHandle': ctypes.c_void_p,
    'basePipelineIndex': ctypes.c_int32,
}
