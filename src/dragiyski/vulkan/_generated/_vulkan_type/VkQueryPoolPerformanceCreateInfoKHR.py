import ctypes

class VkQueryPoolPerformanceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('counterIndexCount', ctypes.c_uint32),
        ('pCounterIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkQueryPoolCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'queueFamilyIndex': 'queue_family_index',
        'counterIndexCount': 'counter_index_count',
        'pCounterIndices': 'counter_indices',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_performance_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkQueryPoolPerformanceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queueFamilyIndex': ctypes.c_uint32,
    'counterIndexCount': ctypes.c_uint32,
    'pCounterIndices': ctypes.POINTER(ctypes.c_uint32),
}
