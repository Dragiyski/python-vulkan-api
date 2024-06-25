import ctypes

class VkExecutionGraphPipelineCreateInfoAMDX(ctypes.Structure):
    pass

from .VkPipelineLibraryCreateInfoKHR import VkPipelineLibraryCreateInfoKHR
from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo

VkExecutionGraphPipelineCreateInfoAMDX._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('pLibraryInfo', ctypes.POINTER(VkPipelineLibraryCreateInfoKHR)),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

VkExecutionGraphPipelineCreateInfoAMDX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stageCount': ctypes.c_uint32,
    'pStages': ctypes.POINTER(VkPipelineShaderStageCreateInfo),
    'pLibraryInfo': ctypes.POINTER(VkPipelineLibraryCreateInfoKHR),
    'layout': ctypes.c_void_p,
    'basePipelineHandle': ctypes.c_void_p,
    'basePipelineIndex': ctypes.c_int32,
}
