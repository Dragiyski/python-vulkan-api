import ctypes

class VkPhysicalDeviceNestedCommandBufferFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('nestedCommandBuffer', ctypes.c_uint32),
        ('nestedCommandBufferRendering', ctypes.c_uint32),
        ('nestedCommandBufferSimultaneousUse', ctypes.c_uint32),
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
        'nestedCommandBuffer': 'nested_command_buffer',
        'nestedCommandBufferRendering': 'nested_command_buffer_rendering',
        'nestedCommandBufferSimultaneousUse': 'nested_command_buffer_simultaneous_use',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_nested_command_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_NESTED_COMMAND_BUFFER_FEATURES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_NESTED_COMMAND_BUFFER_FEATURES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceNestedCommandBufferFeaturesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'nestedCommandBuffer': ctypes.c_uint32,
    'nestedCommandBufferRendering': ctypes.c_uint32,
    'nestedCommandBufferSimultaneousUse': ctypes.c_uint32,
}
