import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandPool', ctypes.c_void_p),
        ('level', ctypes.c_int),
        ('commandBufferCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkAllocateCommandBuffers',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_ALLOCATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'commandPool': {'python_name': ['command', 'pool']},
        'level': {'python_name': ['level'], 'type': 'VkCommandBufferLevel'},
        'commandBufferCount': {'python_name': ['command', 'buffer', 'count']},
    }
}
