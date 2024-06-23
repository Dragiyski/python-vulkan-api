import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkSubresourceLayout2KHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBRESOURCE_HOST_MEMCPY_SIZE_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'size': {'python_name': ['size']},
    }
}
