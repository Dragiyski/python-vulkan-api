import ctypes

class VkExternalBufferProperties(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkExternalMemoryProperties',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceExternalBufferProperties',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'externalMemoryProperties': 'external_memory_properties',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXTERNAL_BUFFER_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExternalMemoryProperties import VkExternalMemoryProperties

VkExternalBufferProperties._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('externalMemoryProperties', VkExternalMemoryProperties),
]

VkExternalBufferProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'externalMemoryProperties': VkExternalMemoryProperties,
}
