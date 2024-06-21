import ctypes

class CType(ctypes.Structure):
    pass

from .VkPipelineShaderStageCreateInfo import CType as VkPipelineShaderStageCreateInfo
from .VkPipelineTessellationStateCreateInfo import CType as VkPipelineTessellationStateCreateInfo
from .VkPipelineVertexInputStateCreateInfo import CType as VkPipelineVertexInputStateCreateInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('pVertexInputState', ctypes.POINTER(VkPipelineVertexInputStateCreateInfo)),
    ('pTessellationState', ctypes.POINTER(VkPipelineTessellationStateCreateInfo)),
]
