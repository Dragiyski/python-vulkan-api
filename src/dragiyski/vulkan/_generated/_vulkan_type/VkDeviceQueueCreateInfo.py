import ctypes

class VkDeviceQueueCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('queueCount', ctypes.c_uint32),
        ('pQueuePriorities', ctypes.POINTER(ctypes.c_float)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDeviceQueueGlobalPriorityCreateInfoKHR',
        'VkDeviceQueueShaderCoreControlCreateInfoARM',
    }
    _includes_ = set()
    _included_in_ = {
        'VkDeviceCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'queueFamilyIndex': 'queue_family_index',
        'queueCount': 'queue_count',
        'pQueuePriorities': 'queue_priorities',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDeviceQueueCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceQueueCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'queueFamilyIndex': ctypes.c_uint32,
    'queueCount': ctypes.c_uint32,
    'pQueuePriorities': ctypes.POINTER(ctypes.c_float),
}
