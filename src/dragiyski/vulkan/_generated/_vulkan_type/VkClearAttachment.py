import ctypes

class CType(ctypes.Structure):
    pass

from .VkClearValue import CType as VkClearValue

CType._fields_ = [
    ('aspectMask', ctypes.c_uint32),
    ('colorAttachment', ctypes.c_uint32),
    ('clearValue', VkClearValue),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkClearValue',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdClearAttachments',
    },
    'output_of': set(),
    'member_map': {
        'aspectMask': {'python_name': ['aspect', 'mask'], 'type': 'VkImageAspectFlags'},
        'colorAttachment': {'python_name': ['color', 'attachment']},
        'clearValue': {'python_name': ['clear', 'value'], 'type': 'VkClearValue'},
    }
}
