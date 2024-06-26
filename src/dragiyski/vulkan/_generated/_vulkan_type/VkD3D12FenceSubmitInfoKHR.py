import ctypes

class VkD3D12FenceSubmitInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreValuesCount', ctypes.c_uint32),
        ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
        ('signalSemaphoreValuesCount', ctypes.c_uint32),
        ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
    ]

    _init_ = []
    _extends_ = {
        'VkSubmitInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'waitSemaphoreValuesCount': 'wait_semaphore_values_count',
        'pWaitSemaphoreValues': 'wait_semaphore_values',
        'signalSemaphoreValuesCount': 'signal_semaphore_values_count',
        'pSignalSemaphoreValues': 'signal_semaphore_values',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_external_semaphore_win32',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_D3D12_FENCE_SUBMIT_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_D3D12_FENCE_SUBMIT_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkD3D12FenceSubmitInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreValuesCount': ctypes.c_uint32,
    'pWaitSemaphoreValues': ctypes.POINTER(ctypes.c_uint64),
    'signalSemaphoreValuesCount': ctypes.c_uint32,
    'pSignalSemaphoreValues': ctypes.POINTER(ctypes.c_uint64),
}
