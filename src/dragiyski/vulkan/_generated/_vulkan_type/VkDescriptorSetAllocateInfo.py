import ctypes

class VkDescriptorSetAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorPool', ctypes.c_void_p),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDescriptorSetVariableDescriptorCountAllocateInfo',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkAllocateDescriptorSets',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'descriptorPool': 'descriptor_pool',
        'descriptorSetCount': 'descriptor_set_count',
        'pSetLayouts': 'set_layouts',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorSetAllocateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'descriptorPool': ctypes.c_void_p,
    'descriptorSetCount': ctypes.c_uint32,
    'pSetLayouts': ctypes.POINTER(ctypes.c_void_p),
}
