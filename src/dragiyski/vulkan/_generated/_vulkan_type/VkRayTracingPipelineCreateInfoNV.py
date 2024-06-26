import ctypes

class VkRayTracingPipelineCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineCreateFlags2CreateInfoKHR',
        'VkPipelineCreationFeedbackCreateInfo',
    }
    _includes_ = {
        'VkPipelineShaderStageCreateInfo',
        'VkRayTracingShaderGroupCreateInfoNV',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateRayTracingPipelinesNV',
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
        'maxRecursionDepth': 'max_recursion_depth',
        'layout': 'layout',
        'basePipelineHandle': 'base_pipeline_handle',
        'basePipelineIndex': 'base_pipeline_index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_ray_tracing',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RAY_TRACING_PIPELINE_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


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
