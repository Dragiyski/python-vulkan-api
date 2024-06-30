from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubmitInfo2'
_member_list_ = ['sType', 'pNext', 'flags', 'waitSemaphoreInfoCount', 'pWaitSemaphoreInfos', 'commandBufferInfoCount', 'pCommandBufferInfos', 'signalSemaphoreInfoCount', 'pSignalSemaphoreInfos']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBMIT_INFO_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSubmitFlags',
        'enum': 'VkSubmitFlags',
        'is_string': False,
    },
    'waitSemaphoreInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pWaitSemaphoreInfos': {
        'type': CPointerType(CComplexType('VkSemaphoreSubmitInfo')),
        'type_name': 'VkSemaphoreSubmitInfo',
        'structure': 'VkSemaphoreSubmitInfo',
        'length': [['waitSemaphoreInfoCount']],
        'is_string': False,
    },
    'commandBufferInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCommandBufferInfos': {
        'type': CPointerType(CComplexType('VkCommandBufferSubmitInfo')),
        'type_name': 'VkCommandBufferSubmitInfo',
        'structure': 'VkCommandBufferSubmitInfo',
        'length': [['commandBufferInfoCount']],
        'is_string': False,
    },
    'signalSemaphoreInfoCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSignalSemaphoreInfos': {
        'type': CPointerType(CComplexType('VkSemaphoreSubmitInfo')),
        'type_name': 'VkSemaphoreSubmitInfo',
        'structure': 'VkSemaphoreSubmitInfo',
        'length': [['signalSemaphoreInfoCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkFrameBoundaryEXT',
    'VkLatencySubmissionPresentIdNV',
    'VkPerformanceQuerySubmitInfoKHR',
    'VkWin32KeyedMutexAcquireReleaseInfoKHR',
    'VkWin32KeyedMutexAcquireReleaseInfoNV',
}
_includes_ = {
    'VkCommandBufferSubmitInfo',
    'VkSemaphoreSubmitInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkQueueSubmit2',
}
_output_of_ = set()
