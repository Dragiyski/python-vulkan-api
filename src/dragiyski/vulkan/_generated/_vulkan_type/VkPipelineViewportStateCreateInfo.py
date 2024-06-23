import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D
from .VkViewport import CType as VkViewport

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('viewportCount', ctypes.c_uint32),
    ('pViewports', ctypes.POINTER(VkViewport)),
    ('scissorCount', ctypes.c_uint32),
    ('pScissors', ctypes.POINTER(VkRect2D)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineViewportCoarseSampleOrderStateCreateInfoNV',
        'VkPipelineViewportDepthClipControlCreateInfoEXT',
        'VkPipelineViewportExclusiveScissorStateCreateInfoNV',
        'VkPipelineViewportShadingRateImageStateCreateInfoNV',
        'VkPipelineViewportSwizzleStateCreateInfoNV',
        'VkPipelineViewportWScalingStateCreateInfoNV',
    },
    'includes': {
        'VkRect2D',
        'VkViewport',
    },
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineViewportStateCreateFlags'},
        'viewportCount': {'python_name': ['viewport', 'count']},
        'pViewports': {'python_name': ['p', 'viewports'], 'len': [['viewportCount']], 'type': 'VkViewport'},
        'scissorCount': {'python_name': ['scissor', 'count']},
        'pScissors': {'python_name': ['p', 'scissors'], 'len': [['scissorCount']], 'type': 'VkRect2D'},
    }
}
