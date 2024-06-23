import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference2 import CType as VkAttachmentReference2
from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pFragmentShadingRateAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('shadingRateAttachmentTexelSize', VkExtent2D),
]

descriptor = {
    'extends': {
        'VkSubpassDescription2',
    },
    'extended_by': set(),
    'includes': {
        'VkAttachmentReference2',
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_FRAGMENT_SHADING_RATE_ATTACHMENT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pFragmentShadingRateAttachment': {'python_name': ['p', 'fragment', 'shading', 'rate', 'attachment'], 'type': 'VkAttachmentReference2'},
        'shadingRateAttachmentTexelSize': {'python_name': ['shading', 'rate', 'attachment', 'texel', 'size'], 'type': 'VkExtent2D'},
    }
}
