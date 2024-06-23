import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreCount', ctypes.c_uint32),
        ('pWaitSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('commandBufferCount', ctypes.c_uint32),
        ('pCommandBufferDeviceMasks', ctypes.POINTER(ctypes.c_uint32)),
        ('signalSemaphoreCount', ctypes.c_uint32),
        ('pSignalSemaphoreDeviceIndices', ctypes.POINTER(ctypes.c_uint32)),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_GROUP_SUBMIT_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'waitSemaphoreCount': {'python_name': ['wait', 'semaphore', 'count']},
        'pWaitSemaphoreDeviceIndices': {'python_name': ['p', 'wait', 'semaphore', 'device', 'indices'], 'len': [['waitSemaphoreCount']]},
        'commandBufferCount': {'python_name': ['command', 'buffer', 'count']},
        'pCommandBufferDeviceMasks': {'python_name': ['p', 'command', 'buffer', 'device', 'masks'], 'len': [['commandBufferCount']]},
        'signalSemaphoreCount': {'python_name': ['signal', 'semaphore', 'count']},
        'pSignalSemaphoreDeviceIndices': {'python_name': ['p', 'signal', 'semaphore', 'device', 'indices'], 'len': [['signalSemaphoreCount']]},
    }
}
