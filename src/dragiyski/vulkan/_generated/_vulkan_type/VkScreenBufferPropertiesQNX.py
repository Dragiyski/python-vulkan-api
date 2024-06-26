import ctypes

class VkScreenBufferPropertiesQNX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkScreenBufferFormatPropertiesQNX',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetScreenBufferPropertiesQNX',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'allocationSize': 'allocation_size',
        'memoryTypeBits': 'memory_type_bits',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_QNX_external_memory_screen_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SCREEN_BUFFER_PROPERTIES_QNX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SCREEN_BUFFER_PROPERTIES_QNX
        for function in self._init_:
            function(self, *args, **kwargs)

VkScreenBufferPropertiesQNX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'allocationSize': ctypes.c_uint64,
    'memoryTypeBits': ctypes.c_uint32,
}
