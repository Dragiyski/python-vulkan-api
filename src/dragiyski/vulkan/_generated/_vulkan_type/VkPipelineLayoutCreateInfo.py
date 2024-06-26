import ctypes

class VkPipelineLayoutCreateInfo(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkBindDescriptorBufferEmbeddedSamplersInfoEXT',
        'VkBindDescriptorSetsInfoKHR',
        'VkPushConstantsInfoKHR',
        'VkPushDescriptorSetInfoKHR',
        'VkPushDescriptorSetWithTemplateInfoKHR',
        'VkSetDescriptorBufferOffsetsInfoEXT',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkPushConstantRange',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreatePipelineLayout',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'setLayoutCount': 'set_layout_count',
        'pSetLayouts': 'set_layouts',
        'pushConstantRangeCount': 'push_constant_range_count',
        'pPushConstantRanges': 'push_constant_ranges',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineLayoutCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPushConstantRange import VkPushConstantRange

VkPipelineLayoutCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
]

VkPipelineLayoutCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'setLayoutCount': ctypes.c_uint32,
    'pSetLayouts': ctypes.POINTER(ctypes.c_void_p),
    'pushConstantRangeCount': ctypes.c_uint32,
    'pPushConstantRanges': ctypes.POINTER(VkPushConstantRange),
}
