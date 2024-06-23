import ctypes

class CType(ctypes.Structure):
    pass

from .VkCommandBufferSubmitInfo import CType as VkCommandBufferSubmitInfo
from .VkSemaphoreSubmitInfo import CType as VkSemaphoreSubmitInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('waitSemaphoreInfoCount', ctypes.c_uint32),
    ('pWaitSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
    ('commandBufferInfoCount', ctypes.c_uint32),
    ('pCommandBufferInfos', ctypes.POINTER(VkCommandBufferSubmitInfo)),
    ('signalSemaphoreInfoCount', ctypes.c_uint32),
    ('pSignalSemaphoreInfos', ctypes.POINTER(VkSemaphoreSubmitInfo)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkFrameBoundaryEXT',
        'VkLatencySubmissionPresentIdNV',
        'VkPerformanceQuerySubmitInfoKHR',
        'VkWin32KeyedMutexAcquireReleaseInfoKHR',
        'VkWin32KeyedMutexAcquireReleaseInfoNV',
    },
    'includes': {
        'VkCommandBufferSubmitInfo',
        'VkSemaphoreSubmitInfo',
    },
    'included_in': set(),
    'input_of': {
        'vkQueueSubmit2',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBMIT_INFO_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkSubmitFlags'},
        'waitSemaphoreInfoCount': {'python_name': ['wait', 'semaphore', 'info', 'count']},
        'pWaitSemaphoreInfos': {'python_name': ['p', 'wait', 'semaphore', 'infos'], 'len': [['waitSemaphoreInfoCount']], 'type': 'VkSemaphoreSubmitInfo'},
        'commandBufferInfoCount': {'python_name': ['command', 'buffer', 'info', 'count']},
        'pCommandBufferInfos': {'python_name': ['p', 'command', 'buffer', 'infos'], 'len': [['commandBufferInfoCount']], 'type': 'VkCommandBufferSubmitInfo'},
        'signalSemaphoreInfoCount': {'python_name': ['signal', 'semaphore', 'info', 'count']},
        'pSignalSemaphoreInfos': {'python_name': ['p', 'signal', 'semaphore', 'infos'], 'len': [['signalSemaphoreInfoCount']], 'type': 'VkSemaphoreSubmitInfo'},
    }
}
