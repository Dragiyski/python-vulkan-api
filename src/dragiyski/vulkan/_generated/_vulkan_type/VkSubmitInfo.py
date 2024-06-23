import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreCount', ctypes.c_uint32),
        ('pWaitSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('pWaitDstStageMask', ctypes.POINTER(ctypes.c_uint32)),
        ('commandBufferCount', ctypes.c_uint32),
        ('pCommandBuffers', ctypes.POINTER(ctypes.c_void_p)),
        ('signalSemaphoreCount', ctypes.c_uint32),
        ('pSignalSemaphores', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkAmigoProfilingSubmitInfoSEC',
        'VkD3D12FenceSubmitInfoKHR',
        'VkDeviceGroupSubmitInfo',
        'VkFrameBoundaryEXT',
        'VkLatencySubmissionPresentIdNV',
        'VkPerformanceQuerySubmitInfoKHR',
        'VkProtectedSubmitInfo',
        'VkTimelineSemaphoreSubmitInfo',
        'VkWin32KeyedMutexAcquireReleaseInfoKHR',
        'VkWin32KeyedMutexAcquireReleaseInfoNV',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkQueueSubmit',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBMIT_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'waitSemaphoreCount': {'python_name': ['wait', 'semaphore', 'count']},
        'pWaitSemaphores': {'python_name': ['p', 'wait', 'semaphores'], 'len': [['waitSemaphoreCount']]},
        'pWaitDstStageMask': {'python_name': ['p', 'wait', 'dst', 'stage', 'mask'], 'len': [['waitSemaphoreCount']], 'type': 'VkPipelineStageFlags'},
        'commandBufferCount': {'python_name': ['command', 'buffer', 'count']},
        'pCommandBuffers': {'python_name': ['p', 'command', 'buffers'], 'len': [['commandBufferCount']]},
        'signalSemaphoreCount': {'python_name': ['signal', 'semaphore', 'count']},
        'pSignalSemaphores': {'python_name': ['p', 'signal', 'semaphores'], 'len': [['signalSemaphoreCount']]},
    }
}
