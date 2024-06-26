import ctypes

class VkDeviceMemoryOverallocationCreateInfoAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('overallocationBehavior', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkDeviceCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'overallocationBehavior': 'overallocation_behavior',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMD_memory_overallocation_behavior',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'overallocationBehavior': 'VkMemoryOverallocationBehaviorAMD',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_OVERALLOCATION_CREATE_INFO_AMD'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEVICE_MEMORY_OVERALLOCATION_CREATE_INFO_AMD
        for function in self._init_:
            function(self, *args, **kwargs)

VkDeviceMemoryOverallocationCreateInfoAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'overallocationBehavior': ctypes.c_int,
}
