import ctypes

class VkPhysicalDeviceVulkanMemoryModelFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('vulkanMemoryModel', ctypes.c_uint32),
        ('vulkanMemoryModelDeviceScope', ctypes.c_uint32),
        ('vulkanMemoryModelAvailabilityVisibilityChains', ctypes.c_uint32),
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
        'vulkanMemoryModel': 'vulkan_memory_model',
        'vulkanMemoryModelDeviceScope': 'vulkan_memory_model_device_scope',
        'vulkanMemoryModelAvailabilityVisibilityChains': 'vulkan_memory_model_availability_visibility_chains',
    }
    _vk_versions_ = {
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_MEMORY_MODEL_FEATURES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_MEMORY_MODEL_FEATURES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceVulkanMemoryModelFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'vulkanMemoryModel': ctypes.c_uint32,
    'vulkanMemoryModelDeviceScope': ctypes.c_uint32,
    'vulkanMemoryModelAvailabilityVisibilityChains': ctypes.c_uint32,
}
