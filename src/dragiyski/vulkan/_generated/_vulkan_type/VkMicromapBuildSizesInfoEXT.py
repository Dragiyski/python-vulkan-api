import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('micromapSize', ctypes.c_uint64),
        ('buildScratchSize', ctypes.c_uint64),
        ('discardable', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetMicromapBuildSizesEXT',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MICROMAP_BUILD_SIZES_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'micromapSize': {'python_name': ['micromap', 'size']},
        'buildScratchSize': {'python_name': ['build', 'scratch', 'size']},
        'discardable': {'python_name': ['discardable']},
    }
}
