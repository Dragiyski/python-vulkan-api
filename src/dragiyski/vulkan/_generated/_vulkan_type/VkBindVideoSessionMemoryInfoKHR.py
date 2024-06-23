import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryBindIndex', ctypes.c_uint32),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('memorySize', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkBindVideoSessionMemoryKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_VIDEO_SESSION_MEMORY_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memoryBindIndex': {'python_name': ['memory', 'bind', 'index']},
        'memory': {'python_name': ['memory']},
        'memoryOffset': {'python_name': ['memory', 'offset']},
        'memorySize': {'python_name': ['memory', 'size']},
    }
}
