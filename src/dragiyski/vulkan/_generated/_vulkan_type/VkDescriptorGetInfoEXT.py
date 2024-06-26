import ctypes

class VkDescriptorGetInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDescriptorDataEXT',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkGetDescriptorEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'type': 'type',
        'data': 'data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_descriptor_buffer',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'type': 'VkDescriptorType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_GET_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_GET_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDescriptorDataEXT import VkDescriptorDataEXT

VkDescriptorGetInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('type', ctypes.c_int),
    ('data', VkDescriptorDataEXT),
]

VkDescriptorGetInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'type': ctypes.c_int,
    'data': VkDescriptorDataEXT,
}
