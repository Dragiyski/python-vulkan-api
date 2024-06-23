import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('semaphoreCount', ctypes.c_uint32),
        ('pSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('pValues', ctypes.POINTER(ctypes.c_uint64)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkWaitSemaphores',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkSemaphoreWaitFlags'},
        'semaphoreCount': {'python_name': ['semaphore', 'count']},
        'pSemaphores': {'python_name': ['p', 'semaphores'], 'len': [['semaphoreCount']]},
        'pValues': {'python_name': ['p', 'values'], 'len': [['semaphoreCount']]},
    }
}
