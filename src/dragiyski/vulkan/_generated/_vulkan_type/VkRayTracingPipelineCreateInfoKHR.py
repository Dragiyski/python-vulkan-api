import ctypes

class VkRayTracingPipelineCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'stageCount': ctypes.c_uint32,
            'pStages': ctypes.POINTER(VkPipelineShaderStageCreateInfo),
            'groupCount': ctypes.c_uint32,
            'pGroups': ctypes.POINTER(VkRayTracingShaderGroupCreateInfoKHR),
            'maxPipelineRayRecursionDepth': ctypes.c_uint32,
            'pLibraryInfo': ctypes.POINTER(VkPipelineLibraryCreateInfoKHR),
            'pLibraryInterface': ctypes.POINTER(VkRayTracingPipelineInterfaceCreateInfoKHR),
            'pDynamicState': ctypes.POINTER(VkPipelineDynamicStateCreateInfo),
            'layout': ctypes.c_void_p,
            'basePipelineHandle': ctypes.c_void_p,
            'basePipelineIndex': ctypes.c_int32,
        }


from .VkPipelineDynamicStateCreateInfo import VkPipelineDynamicStateCreateInfo
from .VkPipelineLibraryCreateInfoKHR import VkPipelineLibraryCreateInfoKHR
from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo
from .VkRayTracingPipelineInterfaceCreateInfoKHR import VkRayTracingPipelineInterfaceCreateInfoKHR
from .VkRayTracingShaderGroupCreateInfoKHR import VkRayTracingShaderGroupCreateInfoKHR

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
