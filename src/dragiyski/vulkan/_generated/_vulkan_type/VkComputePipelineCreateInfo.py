import ctypes

class VkComputePipelineCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkComputePipelineIndirectBufferInfoNV',
        'VkPipelineCompilerControlCreateInfoAMD',
        'VkPipelineCreateFlags2CreateInfoKHR',
        'VkPipelineCreationFeedbackCreateInfo',
        'VkPipelineRobustnessCreateInfoEXT',
        'VkSubpassShadingPipelineCreateInfoHUAWEI',
    }
    _includes_ = {
        'VkPipelineShaderStageCreateInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateComputePipelines',
        'vkGetPipelineIndirectMemoryRequirementsNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'stage': 'stage',
        'layout': 'layout',
        'basePipelineHandle': 'base_pipeline_handle',
        'basePipelineIndex': 'base_pipeline_index',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMPUTE_PIPELINE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo

VkComputePipelineCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', VkPipelineShaderStageCreateInfo),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

VkComputePipelineCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stage': VkPipelineShaderStageCreateInfo,
    'layout': ctypes.c_void_p,
    'basePipelineHandle': ctypes.c_void_p,
    'basePipelineIndex': ctypes.c_int32,
}
