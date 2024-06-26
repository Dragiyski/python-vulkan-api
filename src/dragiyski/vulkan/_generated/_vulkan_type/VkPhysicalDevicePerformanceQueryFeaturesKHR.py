import ctypes

class VkPhysicalDevicePerformanceQueryFeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('performanceCounterQueryPools', ctypes.c_uint32),
        ('performanceCounterMultipleQueryPools', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'performanceCounterQueryPools': 'performance_counter_query_pools',
        'performanceCounterMultipleQueryPools': 'performance_counter_multiple_query_pools',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_performance_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_FEATURES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PERFORMANCE_QUERY_FEATURES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDevicePerformanceQueryFeaturesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'performanceCounterQueryPools': ctypes.c_uint32,
    'performanceCounterMultipleQueryPools': ctypes.c_uint32,
}
