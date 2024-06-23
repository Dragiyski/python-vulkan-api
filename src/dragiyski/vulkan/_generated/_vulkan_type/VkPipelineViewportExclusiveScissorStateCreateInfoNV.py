import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('exclusiveScissorCount', ctypes.c_uint32),
    ('pExclusiveScissors', ctypes.POINTER(VkRect2D)),
]

descriptor = {
    'extends': {
        'VkPipelineViewportStateCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_VIEWPORT_EXCLUSIVE_SCISSOR_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'exclusiveScissorCount': {'python_name': ['exclusive', 'scissor', 'count']},
        'pExclusiveScissors': {'python_name': ['p', 'exclusive', 'scissors'], 'len': [['exclusiveScissorCount']], 'type': 'VkRect2D'},
    }
}
