import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkImagePlaneMemoryRequirementsInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetImageMemoryRequirements2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_MEMORY_REQUIREMENTS_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'image': {'python_name': ['image']},
    }
}
