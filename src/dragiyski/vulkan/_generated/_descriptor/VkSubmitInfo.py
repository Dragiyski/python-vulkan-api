from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubmitInfo'
_member_list_ = ['sType', 'pNext', 'waitSemaphoreCount', 'pWaitSemaphores', 'pWaitDstStageMask', 'commandBufferCount', 'pCommandBuffers', 'signalSemaphoreCount', 'pSignalSemaphores']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SUBMIT_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'waitSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pWaitSemaphores': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['waitSemaphoreCount']],
        'is_string': False,
    },
    'pWaitDstStageMask': {
        'type': CPointerType(CIntType('c_uint32')),
        'type_name': 'VkPipelineStageFlags',
        'enum': 'VkPipelineStageFlags',
        'length': [['waitSemaphoreCount']],
        'is_string': False,
    },
    'commandBufferCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCommandBuffers': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['commandBufferCount']],
        'is_string': False,
    },
    'signalSemaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSignalSemaphores': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['signalSemaphoreCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
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
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkQueueSubmit',
}
_output_of_ = set()
