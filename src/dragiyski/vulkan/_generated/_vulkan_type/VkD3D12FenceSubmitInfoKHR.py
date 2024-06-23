import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreValuesCount', ctypes.c_uint32),
        ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
        ('signalSemaphoreValuesCount', ctypes.c_uint32),
        ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
    ]

descriptor = {
    'extends': {
        'VkSubmitInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_D3D12_FENCE_SUBMIT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'waitSemaphoreValuesCount': {'python_name': ['wait', 'semaphore', 'values', 'count']},
        'pWaitSemaphoreValues': {'python_name': ['p', 'wait', 'semaphore', 'values'], 'len': [['waitSemaphoreValuesCount']]},
        'signalSemaphoreValuesCount': {'python_name': ['signal', 'semaphore', 'values', 'count']},
        'pSignalSemaphoreValues': {'python_name': ['p', 'signal', 'semaphore', 'values'], 'len': [['signalSemaphoreValuesCount']]},
    }
}
