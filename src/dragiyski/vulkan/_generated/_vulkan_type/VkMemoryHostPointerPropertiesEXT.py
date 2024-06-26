import ctypes

class VkMemoryHostPointerPropertiesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetMemoryHostPointerPropertiesEXT',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'memoryTypeBits': 'memory_type_bits',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_external_memory_host',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_HOST_POINTER_PROPERTIES_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_HOST_POINTER_PROPERTIES_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryHostPointerPropertiesEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryTypeBits': ctypes.c_uint32,
}
