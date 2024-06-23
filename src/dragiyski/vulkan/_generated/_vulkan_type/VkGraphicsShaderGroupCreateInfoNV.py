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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkPipelineShaderStageCreateInfo',
        'VkPipelineTessellationStateCreateInfo',
        'VkPipelineVertexInputStateCreateInfo',
    },
    'included_in': {
        'VkGraphicsPipelineShaderGroupsCreateInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_GRAPHICS_SHADER_GROUP_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stageCount': {'python_name': ['stage', 'count']},
        'pStages': {'python_name': ['p', 'stages'], 'len': [['stageCount']], 'type': 'VkPipelineShaderStageCreateInfo'},
        'pVertexInputState': {'python_name': ['p', 'vertex', 'input', 'state'], 'type': 'VkPipelineVertexInputStateCreateInfo'},
        'pTessellationState': {'python_name': ['p', 'tessellation', 'state'], 'type': 'VkPipelineTessellationStateCreateInfo'},
    }
}
