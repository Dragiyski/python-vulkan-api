import ctypes

class VkGraphicsPipelineCreateInfo(ctypes.Structure):
    pass

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
