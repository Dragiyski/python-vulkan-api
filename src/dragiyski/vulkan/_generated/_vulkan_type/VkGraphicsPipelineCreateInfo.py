import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineColorBlendStateCreateInfo import CType as VkPipelineColorBlendStateCreateInfo
from .VkPipelineDepthStencilStateCreateInfo import CType as VkPipelineDepthStencilStateCreateInfo
from .VkPipelineDynamicStateCreateInfo import CType as VkPipelineDynamicStateCreateInfo
from .VkPipelineInputAssemblyStateCreateInfo import CType as VkPipelineInputAssemblyStateCreateInfo
from .VkPipelineMultisampleStateCreateInfo import CType as VkPipelineMultisampleStateCreateInfo
from .VkPipelineRasterizationStateCreateInfo import CType as VkPipelineRasterizationStateCreateInfo
from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo
from .VkPipelineTessellationStateCreateInfo import CType as VkPipelineTessellationStateCreateInfo
from .VkPipelineVertexInputStateCreateInfo import CType as VkPipelineVertexInputStateCreateInfo
from .VkPipelineViewportStateCreateInfo import CType as VkPipelineViewportStateCreateInfo

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': {
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
        'VkPipelineOfflineCreateInfo',
        'VkPipelineRenderingCreateInfo',
        'VkPipelineRepresentativeFragmentTestStateCreateInfoNV',
        'VkPipelineRobustnessCreateInfoEXT',
        'VkRenderingAttachmentLocationInfoKHR',
        'VkRenderingInputAttachmentIndexInfoKHR',
    },
    'includes': {
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
    },
    'included_in': set(),
    'input_of': {
        'vkCreateGraphicsPipelines',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCreateFlags'},
        'stageCount': {'python_name': ['stage', 'count']},
        'pStages': {'python_name': ['p', 'stages'], 'len': [['stageCount']], 'type': 'VkPipelineShaderStageCreateInfo'},
        'pVertexInputState': {'python_name': ['p', 'vertex', 'input', 'state'], 'type': 'VkPipelineVertexInputStateCreateInfo'},
        'pInputAssemblyState': {'python_name': ['p', 'input', 'assembly', 'state'], 'type': 'VkPipelineInputAssemblyStateCreateInfo'},
        'pTessellationState': {'python_name': ['p', 'tessellation', 'state'], 'type': 'VkPipelineTessellationStateCreateInfo'},
        'pViewportState': {'python_name': ['p', 'viewport', 'state'], 'type': 'VkPipelineViewportStateCreateInfo'},
        'pRasterizationState': {'python_name': ['p', 'rasterization', 'state'], 'type': 'VkPipelineRasterizationStateCreateInfo'},
        'pMultisampleState': {'python_name': ['p', 'multisample', 'state'], 'type': 'VkPipelineMultisampleStateCreateInfo'},
        'pDepthStencilState': {'python_name': ['p', 'depth', 'stencil', 'state'], 'type': 'VkPipelineDepthStencilStateCreateInfo'},
        'pColorBlendState': {'python_name': ['p', 'color', 'blend', 'state'], 'type': 'VkPipelineColorBlendStateCreateInfo'},
        'pDynamicState': {'python_name': ['p', 'dynamic', 'state'], 'type': 'VkPipelineDynamicStateCreateInfo'},
        'layout': {'python_name': ['layout']},
        'renderPass': {'python_name': ['render', 'pass']},
        'subpass': {'python_name': ['subpass']},
        'basePipelineHandle': {'python_name': ['base', 'pipeline', 'handle']},
        'basePipelineIndex': {'python_name': ['base', 'pipeline', 'index']},
    }
}
