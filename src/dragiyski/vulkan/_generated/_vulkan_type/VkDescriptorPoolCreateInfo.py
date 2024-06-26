import ctypes

class VkDescriptorPoolCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDescriptorPoolInlineUniformBlockCreateInfo',
        'VkMutableDescriptorTypeCreateInfoEXT',
    }
    _includes_ = {
        'VkDescriptorPoolSize',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateDescriptorPool',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'maxSets': 'max_sets',
        'poolSizeCount': 'pool_size_count',
        'pPoolSizes': 'pool_sizes',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDescriptorPoolCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_POOL_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDescriptorPoolSize import VkDescriptorPoolSize

VkDescriptorPoolCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('maxSets', ctypes.c_uint32),
    ('poolSizeCount', ctypes.c_uint32),
    ('pPoolSizes', ctypes.POINTER(VkDescriptorPoolSize)),
]

VkDescriptorPoolCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'maxSets': ctypes.c_uint32,
    'poolSizeCount': ctypes.c_uint32,
    'pPoolSizes': ctypes.POINTER(VkDescriptorPoolSize),
}
