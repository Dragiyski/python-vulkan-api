import ctypes

class CType(ctypes.Structure):
    pass

from .VkImageSubresourceRange import CType as VkImageSubresourceRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('image', ctypes.c_void_p),
    ('oldLayout', ctypes.c_int),
    ('newLayout', ctypes.c_int),
    ('subresourceRange', VkImageSubresourceRange),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkImageSubresourceRange',
    },
    'included_in': set(),
    'input_of': {
        'vkTransitionImageLayoutEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_HOST_IMAGE_LAYOUT_TRANSITION_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'image': {'python_name': ['image']},
        'oldLayout': {'python_name': ['old', 'layout'], 'type': 'VkImageLayout'},
        'newLayout': {'python_name': ['new', 'layout'], 'type': 'VkImageLayout'},
        'subresourceRange': {'python_name': ['subresource', 'range'], 'type': 'VkImageSubresourceRange'},
    }
}
