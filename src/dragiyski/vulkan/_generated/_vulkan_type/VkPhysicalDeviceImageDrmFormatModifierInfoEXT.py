import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifier', ctypes.c_uint64),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceImageFormatInfo2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_DRM_FORMAT_MODIFIER_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'drmFormatModifier': {'python_name': ['drm', 'format', 'modifier']},
        'sharingMode': {'python_name': ['sharing', 'mode'], 'type': 'VkSharingMode'},
        'queueFamilyIndexCount': {'python_name': ['queue', 'family', 'index', 'count']},
        'pQueueFamilyIndices': {'python_name': ['p', 'queue', 'family', 'indices'], 'len': [['queueFamilyIndexCount']]},
    }
}
