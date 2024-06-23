import ctypes

class CType(ctypes.Structure):
    pass

from .VkDrmFormatModifierPropertiesEXT import CType as VkDrmFormatModifierPropertiesEXT

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('drmFormatModifierCount', ctypes.c_uint32),
    ('pDrmFormatModifierProperties', ctypes.POINTER(VkDrmFormatModifierPropertiesEXT)),
]

descriptor = {
    'extends': {
        'VkFormatProperties2',
    },
    'extended_by': set(),
    'includes': {
        'VkDrmFormatModifierPropertiesEXT',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DRM_FORMAT_MODIFIER_PROPERTIES_LIST_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'drmFormatModifierCount': {'python_name': ['drm', 'format', 'modifier', 'count']},
        'pDrmFormatModifierProperties': {'python_name': ['p', 'drm', 'format', 'modifier', 'properties'], 'len': [['drmFormatModifierCount']], 'type': 'VkDrmFormatModifierPropertiesEXT'},
    }
}
