import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('imageView', ctypes.c_void_p),
    ('imageLayout', ctypes.c_int),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]

descriptor = {
    'extends': {
        'VkRenderingInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDERING_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'imageView': {'python_name': ['image', 'view']},
        'imageLayout': {'python_name': ['image', 'layout'], 'type': 'VkImageLayout'},
        'shadingRateAttachmentTexelSize': {'python_name': ['shading', 'rate', 'attachment', 'texel', 'size'], 'type': 'VkExtent2D'},
    }
}
