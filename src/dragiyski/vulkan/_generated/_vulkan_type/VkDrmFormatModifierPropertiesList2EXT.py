import ctypes

class CType(ctypes.Structure):
    pass

from .VkDrmFormatModifierProperties2EXT import CType as VkDrmFormatModifierProperties2EXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierProperties2EXT)),
]

descriptor = {
    'extends': {
        'VkFormatProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkDrmFormatModifierProperties2EXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_2_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'drmFormatModifierCount': {'python_name': ['drm', 'format', 'modifier', 'count']},
        'pDrmFormatModifierProperties': {'python_name': ['p', 'drm', 'format', 'modifier', 'properties'], 'len': [['drmFormatModifierCount']], 'type': 'VkDrmFormatModifierProperties2EXT'},
    }
}
