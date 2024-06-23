import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphoreType', ctypes.c_int),
        ('initialValue', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceExternalSemaphoreInfo',
        'VkSemaphoreCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'semaphoreType': {'python_name': ['semaphore', 'type'], 'type': 'VkSemaphoreType'},
        'initialValue': {'python_name': ['initial', 'value']},
    }
}
