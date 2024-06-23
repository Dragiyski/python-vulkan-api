import ctypes

class CType(ctypes.Structure):
    pass

from .VkClearValue import CType as VkClearValue

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('resolveMode', ctypes.c_uint32),
    ('resolveImageView', ctypes.c_void_p),
    ('resolveImageLayout', ctypes.c_int),
    ('loadOp', ctypes.c_int),
    ('storeOp', ctypes.c_int),
    ('clearValue', VkClearValue),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkClearValue',
    },
    'included_in': {
        'VkRenderingInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDERING_ATTACHMENT_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageView': {'python_name': ['image', 'view']},
        'imageLayout': {'python_name': ['image', 'layout'], 'type': 'VkImageLayout'},
        'resolveMode': {'python_name': ['resolve', 'mode'], 'type': 'VkResolveModeFlagBits'},
        'resolveImageView': {'python_name': ['resolve', 'image', 'view']},
        'resolveImageLayout': {'python_name': ['resolve', 'image', 'layout'], 'type': 'VkImageLayout'},
        'loadOp': {'python_name': ['load', 'op'], 'type': 'VkAttachmentLoadOp'},
        'storeOp': {'python_name': ['store', 'op'], 'type': 'VkAttachmentStoreOp'},
        'clearValue': {'python_name': ['clear', 'value'], 'type': 'VkClearValue'},
    }
}
