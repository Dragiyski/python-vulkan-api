import ctypes

class VkPerformanceCounterKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('unit', ctypes.c_int),
        ('scope', ctypes.c_int),
        ('storage', ctypes.c_int),
        ('uuid', ctypes.ARRAY(ctypes.c_uint8, 16)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'unit': 'unit',
        'scope': 'scope',
        'storage': 'storage',
        'uuid': 'uuid',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_performance_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'unit': 'VkPerformanceCounterUnitKHR',
        'scope': 'VkPerformanceCounterScopeKHR',
        'storage': 'VkPerformanceCounterStorageKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPerformanceCounterKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'unit': ctypes.c_int,
    'scope': ctypes.c_int,
    'storage': ctypes.c_int,
    'uuid': ctypes.ARRAY(ctypes.c_uint8, 16),
}
