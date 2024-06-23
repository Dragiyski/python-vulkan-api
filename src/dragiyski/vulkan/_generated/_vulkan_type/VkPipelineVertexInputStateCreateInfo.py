import ctypes

class CType(ctypes.Structure):
    pass

from .VkVertexInputAttributeDescription import CType as VkVertexInputAttributeDescription
from .VkVertexInputBindingDescription import CType as VkVertexInputBindingDescription

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('vertexBindingDescriptionCount', ctypes.c_uint32),
    ('pVertexBindingDescriptions', ctypes.POINTER(VkVertexInputBindingDescription)),
    ('vertexAttributeDescriptionCount', ctypes.c_uint32),
    ('pVertexAttributeDescriptions', ctypes.POINTER(VkVertexInputAttributeDescription)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineVertexInputDivisorStateCreateInfoKHR',
    },
    'includes': {
        'VkVertexInputAttributeDescription',
        'VkVertexInputBindingDescription',
    },
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
        'VkGraphicsShaderGroupCreateInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VERTEX_INPUT_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineVertexInputStateCreateFlags'},
        'vertexBindingDescriptionCount': {'python_name': ['vertex', 'binding', 'description', 'count']},
        'pVertexBindingDescriptions': {'python_name': ['p', 'vertex', 'binding', 'descriptions'], 'len': [['vertexBindingDescriptionCount']], 'type': 'VkVertexInputBindingDescription'},
        'vertexAttributeDescriptionCount': {'python_name': ['vertex', 'attribute', 'description', 'count']},
        'pVertexAttributeDescriptions': {'python_name': ['p', 'vertex', 'attribute', 'descriptions'], 'len': [['vertexAttributeDescriptionCount']], 'type': 'VkVertexInputAttributeDescription'},
    }
}
