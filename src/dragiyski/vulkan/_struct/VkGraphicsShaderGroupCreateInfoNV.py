import ctypes, sys

class VkGraphicsShaderGroupCreateInfoNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkGraphicsShaderGroupCreateInfoNV

from . import VkPipelineTessellationStateCreateInfo
from . import VkPipelineVertexInputStateCreateInfo
from . import VkPipelineShaderStageCreateInfo

VkGraphicsShaderGroupCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('pVertexInputState', ctypes.POINTER(VkPipelineVertexInputStateCreateInfo)),
    ('pTessellationState', ctypes.POINTER(VkPipelineTessellationStateCreateInfo)),
]
