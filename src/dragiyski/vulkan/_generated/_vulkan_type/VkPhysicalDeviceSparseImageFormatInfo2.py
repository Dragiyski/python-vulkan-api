import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('type', ctypes.c_int),
        ('samples', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('tiling', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceSparseImageFormatProperties2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SPARSE_IMAGE_FORMAT_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'type': {'python_name': ['type'], 'type': 'VkImageType'},
        'samples': {'python_name': ['samples'], 'type': 'VkSampleCountFlagBits'},
        'usage': {'python_name': ['usage'], 'type': 'VkImageUsageFlags'},
        'tiling': {'python_name': ['tiling'], 'type': 'VkImageTiling'},
    }
}
