import ctypes

class CType(ctypes.Structure):
    pass

from .VkAttachmentReference import CType as VkAttachmentReference

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityMapAttachment', VkAttachmentReference),
]

descriptor = {
    'extends': {
        'VkRenderPassCreateInfo',
        'VkRenderPassCreateInfo2',
    },
    'extended_by': set(),
    'includes': {
        'VkAttachmentReference',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_RENDER_PASS_FRAGMENT_DENSITY_MAP_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fragmentDensityMapAttachment': {'python_name': ['fragment', 'density', 'map', 'attachment'], 'type': 'VkAttachmentReference'},
    }
}
