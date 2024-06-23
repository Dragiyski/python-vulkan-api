import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkFlushMappedMemoryRanges',
        'vkInvalidateMappedMemoryRanges',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MAPPED_MEMORY_RANGE', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memory': {'python_name': ['memory']},
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
    }
}
