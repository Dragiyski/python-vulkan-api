import ctypes

class VkValidationCacheCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('initialDataSize', ctypes.c_size_t),
        ('pInitialData', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateValidationCacheEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'initialDataSize': 'initial_data_size',
        'pInitialData': 'initial_data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_validation_cache',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkValidationCacheCreateFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VALIDATION_CACHE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VALIDATION_CACHE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkValidationCacheCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'initialDataSize': ctypes.c_size_t,
    'pInitialData': ctypes.c_void_p,
}
