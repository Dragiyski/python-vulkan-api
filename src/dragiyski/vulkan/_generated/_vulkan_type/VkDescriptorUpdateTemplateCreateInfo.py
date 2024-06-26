import ctypes

class VkDescriptorUpdateTemplateCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkDescriptorUpdateTemplateEntry',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateDescriptorUpdateTemplate',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'descriptorUpdateEntryCount': 'descriptor_update_entry_count',
        'pDescriptorUpdateEntries': 'descriptor_update_entries',
        'templateType': 'template_type',
        'descriptorSetLayout': 'descriptor_set_layout',
        'pipelineBindPoint': 'pipeline_bind_point',
        'pipelineLayout': 'pipeline_layout',
        'set': 'set',
    }
    _vk_versions_ = {
        (1, 1),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkDescriptorUpdateTemplateCreateFlags',
        'templateType': 'VkDescriptorUpdateTemplateType',
        'pipelineBindPoint': 'VkPipelineBindPoint',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkDescriptorUpdateTemplateEntry import VkDescriptorUpdateTemplateEntry

VkDescriptorUpdateTemplateCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('descriptorUpdateEntryCount', ctypes.c_uint32),
    ('pDescriptorUpdateEntries', ctypes.POINTER(VkDescriptorUpdateTemplateEntry)),
    ('templateType', ctypes.c_int),
    ('descriptorSetLayout', ctypes.c_void_p),
    ('pipelineBindPoint', ctypes.c_int),
    ('pipelineLayout', ctypes.c_void_p),
    ('set', ctypes.c_uint32),
]

VkDescriptorUpdateTemplateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'descriptorUpdateEntryCount': ctypes.c_uint32,
    'pDescriptorUpdateEntries': ctypes.POINTER(VkDescriptorUpdateTemplateEntry),
    'templateType': ctypes.c_int,
    'descriptorSetLayout': ctypes.c_void_p,
    'pipelineBindPoint': ctypes.c_int,
    'pipelineLayout': ctypes.c_void_p,
    'set': ctypes.c_uint32,
}
