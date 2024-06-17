import ctypes, sys

class VkRayTracingPipelineCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkRayTracingPipelineCreateInfoKHR

from . import VkPipelineDynamicStateCreateInfo
from . import VkPipelineLibraryCreateInfoKHR
from . import VkPipelineShaderStageCreateInfo
from . import VkRayTracingPipelineInterfaceCreateInfoKHR
from . import VkRayTracingShaderGroupCreateInfoKHR

VkRayTracingPipelineCreateInfoKHR._fields_ = [
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
