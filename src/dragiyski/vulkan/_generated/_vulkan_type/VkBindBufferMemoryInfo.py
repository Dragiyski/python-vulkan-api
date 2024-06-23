import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkBindBufferMemoryDeviceGroupInfo',
        'VkBindMemoryStatusKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkBindBufferMemory2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'buffer': {'python_name': ['buffer']},
        'memory': {'python_name': ['memory']},
        'memoryOffset': {'python_name': ['memory', 'offset']},
    }
}
