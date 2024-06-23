import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandPoolReservedSize', ctypes.c_uint64),
        ('commandPoolMaxCommandBuffers', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkCommandPoolCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_POOL_MEMORY_RESERVATION_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'commandPoolReservedSize': {'python_name': ['command', 'pool', 'reserved', 'size']},
        'commandPoolMaxCommandBuffers': {'python_name': ['command', 'pool', 'max', 'command', 'buffers']},
    }
}
