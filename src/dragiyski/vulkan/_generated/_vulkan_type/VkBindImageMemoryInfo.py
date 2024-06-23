import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('image', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkBindImageMemoryDeviceGroupInfo',
        'VkBindImageMemorySwapchainInfoKHR',
        'VkBindImagePlaneMemoryInfo',
        'VkBindMemoryStatusKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkBindImageMemory2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_IMAGE_MEMORY_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'image': {'python_name': ['image']},
        'memory': {'python_name': ['memory']},
        'memoryOffset': {'python_name': ['memory', 'offset']},
    }
}
