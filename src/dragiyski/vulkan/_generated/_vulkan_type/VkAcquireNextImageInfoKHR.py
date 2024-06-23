import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchain', ctypes.c_void_p),
        ('timeout', ctypes.c_uint64),
        ('semaphore', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('deviceMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkAcquireNextImage2KHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ACQUIRE_NEXT_IMAGE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'swapchain': {'python_name': ['swapchain'], 'externsync': [['true']]},
        'timeout': {'python_name': ['timeout']},
        'semaphore': {'python_name': ['semaphore'], 'externsync': [['true']]},
        'fence': {'python_name': ['fence'], 'externsync': [['true']]},
        'deviceMask': {'python_name': ['device', 'mask']},
    }
}
