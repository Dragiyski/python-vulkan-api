import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('planeAspect', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkBindImageMemoryInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_IMAGE_PLANE_MEMORY_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'planeAspect': {'python_name': ['plane', 'aspect'], 'type': 'VkImageAspectFlagBits'},
    }
}
