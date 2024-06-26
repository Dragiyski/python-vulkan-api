import ctypes

class VkSubmitInfo(ctypes.Structure):
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

    _init_ = []
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
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'waitSemaphoreCount': 'wait_semaphore_count',
        'pWaitSemaphores': 'wait_semaphores',
        'pWaitDstStageMask': 'wait_dst_stage_mask',
        'commandBufferCount': 'command_buffer_count',
        'pCommandBuffers': 'command_buffers',
        'signalSemaphoreCount': 'signal_semaphore_count',
        'pSignalSemaphores': 'signal_semaphores',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pWaitDstStageMask': 'VkPipelineStageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SUBMIT_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBMIT_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSubmitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreCount': ctypes.c_uint32,
    'pWaitSemaphores': ctypes.POINTER(ctypes.c_void_p),
    'pWaitDstStageMask': ctypes.POINTER(ctypes.c_uint32),
    'commandBufferCount': ctypes.c_uint32,
    'pCommandBuffers': ctypes.POINTER(ctypes.c_void_p),
    'signalSemaphoreCount': ctypes.c_uint32,
    'pSignalSemaphores': ctypes.POINTER(ctypes.c_void_p),
}
