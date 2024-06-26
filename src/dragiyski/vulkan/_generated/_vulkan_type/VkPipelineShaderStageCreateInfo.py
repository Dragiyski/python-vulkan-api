import ctypes

class VkPipelineShaderStageCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDebugUtilsObjectNameInfoEXT',
        'VkPipelineRobustnessCreateInfoEXT',
        'VkPipelineShaderStageModuleIdentifierCreateInfoEXT',
        'VkPipelineShaderStageNodeCreateInfoAMDX',
        'VkPipelineShaderStageRequiredSubgroupSizeCreateInfo',
        'VkShaderModuleCreateInfo',
        'VkShaderModuleValidationCacheCreateInfoEXT',
    }
    _includes_ = {
        'VkSpecializationInfo',
    }
    _included_in_ = {
        'VkComputePipelineCreateInfo',
        'VkExecutionGraphPipelineCreateInfoAMDX',
        'VkGraphicsPipelineCreateInfo',
        'VkGraphicsShaderGroupCreateInfoNV',
        'VkRayTracingPipelineCreateInfoKHR',
        'VkRayTracingPipelineCreateInfoNV',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'stage': 'stage',
        'module': 'module',
        'pName': 'name',
        'pSpecializationInfo': 'specialization_info',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineShaderStageCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkSpecializationInfo import VkSpecializationInfo

VkPipelineShaderStageCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', ctypes.c_uint32),
    ('module', ctypes.c_void_p),
    ('pName', ctypes.c_char_p),
    ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo)),
]

VkPipelineShaderStageCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stage': ctypes.c_uint32,
    'module': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
    'pSpecializationInfo': ctypes.POINTER(VkSpecializationInfo),
}
