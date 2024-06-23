import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('collection', ctypes.c_void_p),
        ('index', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkBufferCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_COLLECTION_BUFFER_CREATE_INFO_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'collection': {'python_name': ['collection']},
        'index': {'python_name': ['index']},
    }
}
