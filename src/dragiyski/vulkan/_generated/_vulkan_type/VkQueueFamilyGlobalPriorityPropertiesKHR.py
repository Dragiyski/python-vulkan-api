import ctypes

class VkQueueFamilyGlobalPriorityPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('priorityCount', ctypes.c_uint32),
        ('priorities', ctypes.ARRAY(ctypes.c_int, 16)),
    ]

    _init_ = []
    _extends_ = {
        'VkQueueFamilyProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'priorityCount': 'priority_count',
        'priorities': 'priorities',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_global_priority',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'priorities': 'VkQueueGlobalPriorityKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_QUEUE_FAMILY_GLOBAL_PRIORITY_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_QUEUE_FAMILY_GLOBAL_PRIORITY_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkQueueFamilyGlobalPriorityPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'priorityCount': ctypes.c_uint32,
    'priorities': ctypes.ARRAY(ctypes.c_int, 16),
}
