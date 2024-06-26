import ctypes

class VkDeviceQueueGlobalPriorityCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('globalPriority', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceQueueCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'globalPriority': 'global_priority',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_global_priority',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'globalPriority': 'VkQueueGlobalPriorityKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_GLOBAL_PRIORITY_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_QUEUE_GLOBAL_PRIORITY_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceQueueGlobalPriorityCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'globalPriority': ctypes.c_int,
}
