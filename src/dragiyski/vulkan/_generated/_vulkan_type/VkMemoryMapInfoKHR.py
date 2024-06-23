import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('memory', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkMemoryMapPlacedInfoEXT',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkMapMemory2KHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MEMORY_MAP_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkMemoryMapFlags'},
        'memory': {'python_name': ['memory'], 'externsync': [['true']]},
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
    }
}
