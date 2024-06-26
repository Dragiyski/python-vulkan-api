import ctypes

class VkBindBufferMemoryInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkBindBufferMemoryDeviceGroupInfo',
        'VkBindMemoryStatusKHR',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkBindBufferMemory2',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'buffer': 'buffer',
        'memory': 'memory',
        'memoryOffset': 'memory_offset',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_BUFFER_MEMORY_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkBindBufferMemoryInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'buffer': ctypes.c_void_p,
    'memory': ctypes.c_void_p,
    'memoryOffset': ctypes.c_uint64,
}
