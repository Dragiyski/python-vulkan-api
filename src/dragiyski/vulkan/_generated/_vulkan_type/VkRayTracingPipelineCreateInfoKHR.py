import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineDynamicStateCreateInfo import CType as VkPipelineDynamicStateCreateInfo
from .VkPipelineLibraryCreateInfoKHR import CType as VkPipelineLibraryCreateInfoKHR
from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo
from .VkRayTracingPipelineInterfaceCreateInfoKHR import CType as VkRayTracingPipelineInterfaceCreateInfoKHR
from .VkRayTracingShaderGroupCreateInfoKHR import CType as VkRayTracingShaderGroupCreateInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkRayTracingShaderGroupCreateInfoKHR)),
    ('maxPipelineRayRecursionDepth', ctypes.c_uint32),
    ('pLibraryInfo', ctypes.POINTER(VkPipelineLibraryCreateInfoKHR)),
    ('pLibraryInterface', ctypes.POINTER(VkRayTracingPipelineInterfaceCreateInfoKHR)),
    ('pDynamicState', ctypes.POINTER(VkPipelineDynamicStateCreateInfo)),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]
