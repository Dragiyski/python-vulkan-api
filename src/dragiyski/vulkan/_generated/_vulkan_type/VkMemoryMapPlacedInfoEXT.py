import ctypes

class VkMemoryMapPlacedInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pPlacedAddress', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = {
        'VkMemoryMapInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pPlacedAddress': 'placed_address',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_map_memory_placed',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MEMORY_MAP_PLACED_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MEMORY_MAP_PLACED_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryMapPlacedInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pPlacedAddress': ctypes.c_void_p,
}
