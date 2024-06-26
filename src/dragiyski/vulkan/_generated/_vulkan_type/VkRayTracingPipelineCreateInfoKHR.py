import ctypes

class VkRayTracingPipelineCreateInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineCreateFlags2CreateInfoKHR',
        'VkPipelineCreationFeedbackCreateInfo',
        'VkPipelineRobustnessCreateInfoEXT',
    }
    _includes_ = {
        'VkPipelineDynamicStateCreateInfo',
        'VkPipelineLibraryCreateInfoKHR',
        'VkPipelineShaderStageCreateInfo',
        'VkRayTracingPipelineInterfaceCreateInfoKHR',
        'VkRayTracingShaderGroupCreateInfoKHR',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateRayTracingPipelinesKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'stageCount': 'stage_count',
        'pStages': 'stages',
        'groupCount': 'group_count',
        'pGroups': 'groups',
        'maxPipelineRayRecursionDepth': 'max_pipeline_ray_recursion_depth',
        'pLibraryInfo': 'library_info',
        'pLibraryInterface': 'library_interface',
        'pDynamicState': 'dynamic_state',
        'layout': 'layout',
        'basePipelineHandle': 'base_pipeline_handle',
        'basePipelineIndex': 'base_pipeline_index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_ray_tracing_pipeline',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


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

VkRayTracingPipelineCreateInfoKHR._type_ = {
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
