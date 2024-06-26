import ctypes

class VkQueryPoolPerformanceQueryCreateInfoINTEL(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('performanceCountersSampling', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkQueryPoolCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'performanceCountersSampling': 'performance_counters_sampling',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_INTEL_performance_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'performanceCountersSampling': 'VkQueryPoolSamplingModeINTEL',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL
        for function in self._init_:
            function(self, *args, **kwargs)

VkQueryPoolPerformanceQueryCreateInfoINTEL._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'performanceCountersSampling': ctypes.c_int,
}
