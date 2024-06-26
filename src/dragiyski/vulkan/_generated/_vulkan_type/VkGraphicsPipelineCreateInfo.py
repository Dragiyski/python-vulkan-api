import ctypes

class VkGraphicsPipelineCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAttachmentSampleCountInfoAMD',
        'VkExternalFormatANDROID',
        'VkGraphicsPipelineLibraryCreateInfoEXT',
        'VkGraphicsPipelineShaderGroupsCreateInfoNV',
        'VkMultiviewPerViewAttributesInfoNVX',
        'VkPipelineCompilerControlCreateInfoAMD',
        'VkPipelineCreateFlags2CreateInfoKHR',
        'VkPipelineCreationFeedbackCreateInfo',
        'VkPipelineDiscardRectangleStateCreateInfoEXT',
        'VkPipelineFragmentShadingRateEnumStateCreateInfoNV',
        'VkPipelineFragmentShadingRateStateCreateInfoKHR',
        'VkPipelineLibraryCreateInfoKHR',
        'VkPipelineRenderingCreateInfo',
        'VkPipelineRepresentativeFragmentTestStateCreateInfoNV',
        'VkPipelineRobustnessCreateInfoEXT',
        'VkRenderingAttachmentLocationInfoKHR',
        'VkRenderingInputAttachmentIndexInfoKHR',
    }
    _includes_ = {
        'VkPipelineColorBlendStateCreateInfo',
        'VkPipelineDepthStencilStateCreateInfo',
        'VkPipelineDynamicStateCreateInfo',
        'VkPipelineInputAssemblyStateCreateInfo',
        'VkPipelineMultisampleStateCreateInfo',
        'VkPipelineRasterizationStateCreateInfo',
        'VkPipelineShaderStageCreateInfo',
        'VkPipelineTessellationStateCreateInfo',
        'VkPipelineVertexInputStateCreateInfo',
        'VkPipelineViewportStateCreateInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateGraphicsPipelines',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'stageCount': 'stage_count',
        'pStages': 'stages',
        'pVertexInputState': 'vertex_input_state',
        'pInputAssemblyState': 'input_assembly_state',
        'pTessellationState': 'tessellation_state',
        'pViewportState': 'viewport_state',
        'pRasterizationState': 'rasterization_state',
        'pMultisampleState': 'multisample_state',
        'pDepthStencilState': 'depth_stencil_state',
        'pColorBlendState': 'color_blend_state',
        'pDynamicState': 'dynamic_state',
        'layout': 'layout',
        'renderPass': 'render_pass',
        'subpass': 'subpass',
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
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPipelineColorBlendStateCreateInfo import VkPipelineColorBlendStateCreateInfo
from .VkPipelineDepthStencilStateCreateInfo import VkPipelineDepthStencilStateCreateInfo
from .VkPipelineDynamicStateCreateInfo import VkPipelineDynamicStateCreateInfo
from .VkPipelineInputAssemblyStateCreateInfo import VkPipelineInputAssemblyStateCreateInfo
from .VkPipelineMultisampleStateCreateInfo import VkPipelineMultisampleStateCreateInfo
from .VkPipelineRasterizationStateCreateInfo import VkPipelineRasterizationStateCreateInfo
from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo
from .VkPipelineTessellationStateCreateInfo import VkPipelineTessellationStateCreateInfo
from .VkPipelineVertexInputStateCreateInfo import VkPipelineVertexInputStateCreateInfo
from .VkPipelineViewportStateCreateInfo import VkPipelineViewportStateCreateInfo

VkGraphicsPipelineCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('pVertexInputState', ctypes.POINTER(VkPipelineVertexInputStateCreateInfo)),
    ('pInputAssemblyState', ctypes.POINTER(VkPipelineInputAssemblyStateCreateInfo)),
    ('pTessellationState', ctypes.POINTER(VkPipelineTessellationStateCreateInfo)),
    ('pViewportState', ctypes.POINTER(VkPipelineViewportStateCreateInfo)),
    ('pRasterizationState', ctypes.POINTER(VkPipelineRasterizationStateCreateInfo)),
    ('pMultisampleState', ctypes.POINTER(VkPipelineMultisampleStateCreateInfo)),
    ('pDepthStencilState', ctypes.POINTER(VkPipelineDepthStencilStateCreateInfo)),
    ('pColorBlendState', ctypes.POINTER(VkPipelineColorBlendStateCreateInfo)),
    ('pDynamicState', ctypes.POINTER(VkPipelineDynamicStateCreateInfo)),
    ('layout', ctypes.c_void_p),
    ('renderPass', ctypes.c_void_p),
    ('subpass', ctypes.c_uint32),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

VkGraphicsPipelineCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stageCount': ctypes.c_uint32,
    'pStages': ctypes.POINTER(VkPipelineShaderStageCreateInfo),
    'pVertexInputState': ctypes.POINTER(VkPipelineVertexInputStateCreateInfo),
    'pInputAssemblyState': ctypes.POINTER(VkPipelineInputAssemblyStateCreateInfo),
    'pTessellationState': ctypes.POINTER(VkPipelineTessellationStateCreateInfo),
    'pViewportState': ctypes.POINTER(VkPipelineViewportStateCreateInfo),
    'pRasterizationState': ctypes.POINTER(VkPipelineRasterizationStateCreateInfo),
    'pMultisampleState': ctypes.POINTER(VkPipelineMultisampleStateCreateInfo),
    'pDepthStencilState': ctypes.POINTER(VkPipelineDepthStencilStateCreateInfo),
    'pColorBlendState': ctypes.POINTER(VkPipelineColorBlendStateCreateInfo),
    'pDynamicState': ctypes.POINTER(VkPipelineDynamicStateCreateInfo),
    'layout': ctypes.c_void_p,
    'renderPass': ctypes.c_void_p,
    'subpass': ctypes.c_uint32,
    'basePipelineHandle': ctypes.c_void_p,
    'basePipelineIndex': ctypes.c_int32,
}
