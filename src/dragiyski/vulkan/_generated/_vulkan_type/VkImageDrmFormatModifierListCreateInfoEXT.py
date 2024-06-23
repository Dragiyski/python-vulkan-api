import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifierCount', ctypes.c_uint32),
        ('pDrmFormatModifiers', ctypes.POINTER(ctypes.c_uint64)),
    ]

descriptor = {
    'extends': {
        'VkImageCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_DRM_FORMAT_MODIFIER_LIST_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'drmFormatModifierCount': {'python_name': ['drm', 'format', 'modifier', 'count']},
        'pDrmFormatModifiers': {'python_name': ['p', 'drm', 'format', 'modifiers'], 'len': [['drmFormatModifierCount']]},
    }
}
