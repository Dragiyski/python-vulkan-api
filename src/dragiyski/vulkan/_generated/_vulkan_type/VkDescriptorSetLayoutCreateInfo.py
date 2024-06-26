import ctypes

class VkDescriptorSetLayoutCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDescriptorSetLayoutBindingFlagsCreateInfo',
        'VkMutableDescriptorTypeCreateInfoEXT',
    }
    _includes_ = {
        'VkDescriptorSetLayoutBinding',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateDescriptorSetLayout',
        'vkGetDescriptorSetLayoutSupport',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'bindingCount': 'binding_count',
        'pBindings': 'bindings',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDescriptorSetLayoutCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDescriptorSetLayoutBinding import VkDescriptorSetLayoutBinding

VkDescriptorSetLayoutCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('bindingCount', ctypes.c_uint32),
    ('pBindings', ctypes.POINTER(VkDescriptorSetLayoutBinding)),
]

VkDescriptorSetLayoutCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'bindingCount': ctypes.c_uint32,
    'pBindings': ctypes.POINTER(VkDescriptorSetLayoutBinding),
}
