import ctypes

class VkMutableDescriptorTypeCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkDescriptorPoolCreateInfo',
        'VkDescriptorSetLayoutCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkMutableDescriptorTypeListEXT',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'mutableDescriptorTypeListCount': 'mutable_descriptor_type_list_count',
        'pMutableDescriptorTypeLists': 'mutable_descriptor_type_lists',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_mutable_descriptor_type',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_MUTABLE_DESCRIPTOR_TYPE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_MUTABLE_DESCRIPTOR_TYPE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkMutableDescriptorTypeListEXT import VkMutableDescriptorTypeListEXT

VkMutableDescriptorTypeCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mutableDescriptorTypeListCount', ctypes.c_uint32),
    ('pMutableDescriptorTypeLists', ctypes.POINTER(VkMutableDescriptorTypeListEXT)),
]

VkMutableDescriptorTypeCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mutableDescriptorTypeListCount': ctypes.c_uint32,
    'pMutableDescriptorTypeLists': ctypes.POINTER(VkMutableDescriptorTypeListEXT),
}
