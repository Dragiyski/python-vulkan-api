import ctypes

class VkTimelineSemaphoreSubmitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('waitSemaphoreValueCount', ctypes.c_uint32),
        ('pWaitSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
        ('signalSemaphoreValueCount', ctypes.c_uint32),
        ('pSignalSemaphoreValues', ctypes.POINTER(ctypes.c_uint64)),
    ]

    _init_ = []
    _extends_ = {
        'VkBindSparseInfo',
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
        'waitSemaphoreValueCount': 'wait_semaphore_value_count',
        'pWaitSemaphoreValues': 'wait_semaphore_values',
        'signalSemaphoreValueCount': 'signal_semaphore_value_count',
        'pSignalSemaphoreValues': 'signal_semaphore_values',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkTimelineSemaphoreSubmitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'waitSemaphoreValueCount': ctypes.c_uint32,
    'pWaitSemaphoreValues': ctypes.POINTER(ctypes.c_uint64),
    'signalSemaphoreValueCount': ctypes.c_uint32,
    'pSignalSemaphoreValues': ctypes.POINTER(ctypes.c_uint64),
}
