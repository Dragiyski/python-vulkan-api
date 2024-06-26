import ctypes

class VkPerformanceCounterDescriptionKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('category', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
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
        'flags': 'flags',
        'name': 'name',
        'category': 'category',
        'description': 'description',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_performance_query',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPerformanceCounterDescriptionFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkPerformanceCounterDescriptionKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'name': ctypes.ARRAY(ctypes.c_char, 256),
    'category': ctypes.ARRAY(ctypes.c_char, 256),
    'description': ctypes.ARRAY(ctypes.c_char, 256),
}
