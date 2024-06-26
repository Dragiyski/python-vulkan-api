import ctypes

class VkAcquireProfilingLockInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('timeout', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkAcquireProfilingLockKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'timeout': 'timeout',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_performance_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkAcquireProfilingLockFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ACQUIRE_PROFILING_LOCK_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ACQUIRE_PROFILING_LOCK_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkAcquireProfilingLockInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'timeout': ctypes.c_uint64,
}
