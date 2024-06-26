import ctypes

class VkPhysicalDeviceMemoryProperties2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPhysicalDeviceMemoryBudgetPropertiesEXT',
    }
    _includes_ = {
        'VkPhysicalDeviceMemoryProperties',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceMemoryProperties2',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'memoryProperties': 'memory_properties',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_PROPERTIES_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPhysicalDeviceMemoryProperties import VkPhysicalDeviceMemoryProperties

VkPhysicalDeviceMemoryProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryProperties', VkPhysicalDeviceMemoryProperties),
]

VkPhysicalDeviceMemoryProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryProperties': VkPhysicalDeviceMemoryProperties,
}
