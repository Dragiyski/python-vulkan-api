import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('acquireUnmodifiedMemory', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkBufferMemoryBarrier',
        'VkBufferMemoryBarrier2',
        'VkImageMemoryBarrier',
        'VkImageMemoryBarrier2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_ACQUIRE_UNMODIFIED_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'acquireUnmodifiedMemory': {'python_name': ['acquire', 'unmodified', 'memory']},
    }
}
