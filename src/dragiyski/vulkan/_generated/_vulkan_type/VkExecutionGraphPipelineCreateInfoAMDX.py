import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineLibraryCreateInfoKHR import CType as VkPipelineLibraryCreateInfoKHR
from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo

CType._fields_ = [
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
