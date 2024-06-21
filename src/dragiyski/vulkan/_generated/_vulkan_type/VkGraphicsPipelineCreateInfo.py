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
