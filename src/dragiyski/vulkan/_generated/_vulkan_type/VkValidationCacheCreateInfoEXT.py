import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('initialDataSize', ctypes.c_size_t),
        ('pInitialData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateValidationCacheEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VALIDATION_CACHE_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkValidationCacheCreateFlagsEXT'},
        'initialDataSize': {'python_name': ['initial', 'data', 'size']},
        'pInitialData': {'python_name': ['p', 'initial', 'data'], 'len': [['initialDataSize']]},
    }
}
