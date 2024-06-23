import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreValueCount', ctypes.c_uint32),
        ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
        ('signalSemaphoreValueCount', ctypes.c_uint32),
        ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
    ]

descriptor = {
    'extends': {
        'VkBindSparseInfo',
        'VkSubmitInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'waitSemaphoreValueCount': {'python_name': ['wait', 'semaphore', 'value', 'count']},
        'pWaitSemaphoreValues': {'python_name': ['p', 'wait', 'semaphore', 'values'], 'len': [['waitSemaphoreValueCount']]},
        'signalSemaphoreValueCount': {'python_name': ['signal', 'semaphore', 'value', 'count']},
        'pSignalSemaphoreValues': {'python_name': ['p', 'signal', 'semaphore', 'values'], 'len': [['signalSemaphoreValueCount']]},
    }
}
