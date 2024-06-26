import ctypes

class VkSemaphoreWaitInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('semaphoreCount', ctypes.c_uint32),
        ('pSemaphores', ctypes.POINTER(ctypes.c_void_p)),
        ('pValues', ctypes.POINTER(ctypes.c_uint64)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkWaitSemaphores',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'semaphoreCount': 'semaphore_count',
        'pSemaphores': 'semaphores',
        'pValues': 'values',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkSemaphoreWaitFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkSemaphoreWaitInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'semaphoreCount': ctypes.c_uint32,
    'pSemaphores': ctypes.POINTER(ctypes.c_void_p),
    'pValues': ctypes.POINTER(ctypes.c_uint64),
}
