import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pResult', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': {
        'VkBindBufferMemoryInfo',
        'VkBindImageMemoryInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_MEMORY_STATUS_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pResult': {'python_name': ['p', 'result'], 'type': 'VkResult'},
    }
}
