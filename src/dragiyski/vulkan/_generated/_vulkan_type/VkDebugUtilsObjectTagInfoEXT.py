import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('tagName', ctypes.c_uint64),
        ('tagSize', ctypes.c_size_t),
        ('pTag', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkSetDebugUtilsObjectTagEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEBUG_UTILS_OBJECT_TAG_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'objectType': {'python_name': ['object', 'type'], 'type': 'VkObjectType'},
        'objectHandle': {'python_name': ['object', 'handle']},
        'tagName': {'python_name': ['tag', 'name']},
        'tagSize': {'python_name': ['tag', 'size']},
        'pTag': {'python_name': ['p', 'tag'], 'len': [['tagSize']]},
    }
}
