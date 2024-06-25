import ctypes

class VkGraphicsShaderGroupCreateInfoNV(ctypes.Structure):
    pass

from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo
from .VkPipelineTessellationStateCreateInfo import VkPipelineTessellationStateCreateInfo
from .VkPipelineVertexInputStateCreateInfo import VkPipelineVertexInputStateCreateInfo

VkGraphicsShaderGroupCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('pVertexInputState', ctypes.POINTER(VkPipelineVertexInputStateCreateInfo)),
    ('pTessellationState', ctypes.POINTER(VkPipelineTessellationStateCreateInfo)),
]

VkGraphicsShaderGroupCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stageCount': ctypes.c_uint32,
    'pStages': ctypes.POINTER(VkPipelineShaderStageCreateInfo),
    'pVertexInputState': ctypes.POINTER(VkPipelineVertexInputStateCreateInfo),
    'pTessellationState': ctypes.POINTER(VkPipelineTessellationStateCreateInfo),
}
