import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('value', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkSignalSemaphore',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_SIGNAL_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'semaphore': {'python_name': ['semaphore']},
        'value': {'python_name': ['value']},
    }
}
