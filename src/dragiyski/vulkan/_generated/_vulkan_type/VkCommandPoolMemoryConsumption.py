import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('commandPoolAllocated', ctypes.c_uint64),
        ('commandPoolReservedSize', ctypes.c_uint64),
        ('commandBufferAllocated', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetCommandPoolMemoryConsumption',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COMMAND_POOL_MEMORY_CONSUMPTION', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'commandPoolAllocated': {'python_name': ['command', 'pool', 'allocated']},
        'commandPoolReservedSize': {'python_name': ['command', 'pool', 'reserved', 'size']},
        'commandBufferAllocated': {'python_name': ['command', 'buffer', 'allocated']},
    }
}
