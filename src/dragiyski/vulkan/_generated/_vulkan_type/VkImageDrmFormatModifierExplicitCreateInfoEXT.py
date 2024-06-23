import ctypes

class CType(ctypes.Structure):
    pass

from .VkSubresourceLayout import CType as VkSubresourceLayout

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifier', ctypes.c_uint64),
    ('drmFormatModifierPlaneCount', ctypes.c_uint32),
    ('pPlaneLayouts', ctypes.POINTER(VkSubresourceLayout)),
]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
    },
    'extended_by': set(),
    'includes': {
        'VkSubresourceLayout',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_EXPLICIT_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'drmFormatModifier': {'python_name': ['drm', 'format', 'modifier']},
        'drmFormatModifierPlaneCount': {'python_name': ['drm', 'format', 'modifier', 'plane', 'count']},
        'pPlaneLayouts': {'python_name': ['p', 'plane', 'layouts'], 'len': [['drmFormatModifierPlaneCount']], 'type': 'VkSubresourceLayout'},
    }
}
