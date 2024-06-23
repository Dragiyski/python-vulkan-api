import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphorePool', ctypes.c_void_p),
        ('pFence', ctypes.POINTER(ctypes.ARRAY(ctypes.c_uint64, 6))),
    ]

descriptor = {
    'extends': {
        'VkSemaphoreCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_SCI_SYNC_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'semaphorePool': {'python_name': ['semaphore', 'pool']},
        'pFence': {'python_name': ['p', 'fence']},
    }
}
