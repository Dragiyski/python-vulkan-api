import ctypes

class CType(ctypes.Structure):
    pass

from .VkRect2D import CType as VkRect2D

CType._fields_ = [
    ('rect', VkRect2D),
    ('baseArrayLayer', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkRect2D',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdClearAttachments',
    },
    'output_of': set(),
    'member_map': {
        'rect': {'python_name': ['rect'], 'type': 'VkRect2D'},
        'baseArrayLayer': {'python_name': ['base', 'array', 'layer']},
        'layerCount': {'python_name': ['layer', 'count']},
    }
}
