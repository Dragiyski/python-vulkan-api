from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGraphicsPipelineCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'stageCount', 'pStages', 'pVertexInputState', 'pInputAssemblyState', 'pTessellationState', 'pViewportState', 'pRasterizationState', 'pMultisampleState', 'pDepthStencilState', 'pColorBlendState', 'pDynamicState', 'layout', 'renderPass', 'subpass', 'basePipelineHandle', 'basePipelineIndex']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPipelineCreateFlags',
        'enum': 'VkPipelineCreateFlags',
        'is_string': False,
    },
    'stageCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStages': {
        'type': CPointerType(CComplexType('VkPipelineShaderStageCreateInfo')),
        'type_name': 'VkPipelineShaderStageCreateInfo',
        'structure': 'VkPipelineShaderStageCreateInfo',
        'length': [['stageCount']],
        'is_string': False,
    },
    'pVertexInputState': {
        'type': CPointerType(CComplexType('VkPipelineVertexInputStateCreateInfo')),
        'type_name': 'VkPipelineVertexInputStateCreateInfo',
        'structure': 'VkPipelineVertexInputStateCreateInfo',
        'is_string': False,
    },
    'pInputAssemblyState': {
        'type': CPointerType(CComplexType('VkPipelineInputAssemblyStateCreateInfo')),
        'type_name': 'VkPipelineInputAssemblyStateCreateInfo',
        'structure': 'VkPipelineInputAssemblyStateCreateInfo',
        'is_string': False,
    },
    'pTessellationState': {
        'type': CPointerType(CComplexType('VkPipelineTessellationStateCreateInfo')),
        'type_name': 'VkPipelineTessellationStateCreateInfo',
        'structure': 'VkPipelineTessellationStateCreateInfo',
        'is_string': False,
    },
    'pViewportState': {
        'type': CPointerType(CComplexType('VkPipelineViewportStateCreateInfo')),
        'type_name': 'VkPipelineViewportStateCreateInfo',
        'structure': 'VkPipelineViewportStateCreateInfo',
        'is_string': False,
    },
    'pRasterizationState': {
        'type': CPointerType(CComplexType('VkPipelineRasterizationStateCreateInfo')),
        'type_name': 'VkPipelineRasterizationStateCreateInfo',
        'structure': 'VkPipelineRasterizationStateCreateInfo',
        'is_string': False,
    },
    'pMultisampleState': {
        'type': CPointerType(CComplexType('VkPipelineMultisampleStateCreateInfo')),
        'type_name': 'VkPipelineMultisampleStateCreateInfo',
        'structure': 'VkPipelineMultisampleStateCreateInfo',
        'is_string': False,
    },
    'pDepthStencilState': {
        'type': CPointerType(CComplexType('VkPipelineDepthStencilStateCreateInfo')),
        'type_name': 'VkPipelineDepthStencilStateCreateInfo',
        'structure': 'VkPipelineDepthStencilStateCreateInfo',
        'is_string': False,
    },
    'pColorBlendState': {
        'type': CPointerType(CComplexType('VkPipelineColorBlendStateCreateInfo')),
        'type_name': 'VkPipelineColorBlendStateCreateInfo',
        'structure': 'VkPipelineColorBlendStateCreateInfo',
        'is_string': False,
    },
    'pDynamicState': {
        'type': CPointerType(CComplexType('VkPipelineDynamicStateCreateInfo')),
        'type_name': 'VkPipelineDynamicStateCreateInfo',
        'structure': 'VkPipelineDynamicStateCreateInfo',
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'renderPass': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'subpass': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'basePipelineHandle': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'basePipelineIndex': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
}
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
