import ctypes, sys

class VkGraphicsPipelineCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkGraphicsPipelineCreateInfo

from . import VkPipelineMultisampleStateCreateInfo
from . import VkPipelineRasterizationStateCreateInfo
from . import VkPipelineShaderStageCreateInfo
from . import VkPipelineColorBlendStateCreateInfo
from . import VkPipelineDynamicStateCreateInfo
from . import VkPipelineViewportStateCreateInfo
from . import VkPipelineDepthStencilStateCreateInfo
from . import VkPipelineVertexInputStateCreateInfo
from . import VkPipelineTessellationStateCreateInfo
from . import VkPipelineInputAssemblyStateCreateInfo

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
