import ctypes

class VkMemoryMapInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('memory', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkMemoryMapPlacedInfoEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkMapMemory2KHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'memory': 'memory',
        'offset': 'offset',
        'size': 'size',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_map_memory2',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkMemoryMapFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_MAP_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_MAP_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryMapInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'memory': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
}
