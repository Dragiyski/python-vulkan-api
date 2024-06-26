import ctypes

class VkSubmitInfo2(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'waitSemaphoreInfoCount': 'wait_semaphore_info_count',
        'pWaitSemaphoreInfos': 'wait_semaphore_infos',
        'commandBufferInfoCount': 'command_buffer_info_count',
        'pCommandBufferInfos': 'command_buffer_infos',
        'signalSemaphoreInfoCount': 'signal_semaphore_info_count',
        'pSignalSemaphoreInfos': 'signal_semaphore_infos',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkSubmitFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SUBMIT_INFO_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBMIT_INFO_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkCommandBufferSubmitInfo import VkCommandBufferSubmitInfo
from .VkSemaphoreSubmitInfo import VkSemaphoreSubmitInfo

VkSubmitInfo2._fields_ = [
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

VkSubmitInfo2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'waitSemaphoreInfoCount': ctypes.c_uint32,
    'pWaitSemaphoreInfos': ctypes.POINTER(VkSemaphoreSubmitInfo),
    'commandBufferInfoCount': ctypes.c_uint32,
    'pCommandBufferInfos': ctypes.POINTER(VkCommandBufferSubmitInfo),
    'signalSemaphoreInfoCount': ctypes.c_uint32,
    'pSignalSemaphoreInfos': ctypes.POINTER(VkSemaphoreSubmitInfo),
}
