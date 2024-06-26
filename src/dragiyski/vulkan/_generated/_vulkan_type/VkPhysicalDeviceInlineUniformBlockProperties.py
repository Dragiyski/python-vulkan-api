import ctypes

class VkPhysicalDeviceInlineUniformBlockProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInlineUniformBlockSize', ctypes.c_uint32),
        ('maxPerStageDescriptorInlineUniformBlocks', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPhysicalDeviceProperties2',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'maxInlineUniformBlockSize': 'max_inline_uniform_block_size',
        'maxPerStageDescriptorInlineUniformBlocks': 'max_per_stage_descriptor_inline_uniform_blocks',
        'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks': 'max_per_stage_descriptor_update_after_bind_inline_uniform_blocks',
        'maxDescriptorSetInlineUniformBlocks': 'max_descriptor_set_inline_uniform_blocks',
        'maxDescriptorSetUpdateAfterBindInlineUniformBlocks': 'max_descriptor_set_update_after_bind_inline_uniform_blocks',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_PROPERTIES'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_PROPERTIES
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceInlineUniformBlockProperties._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxInlineUniformBlockSize': ctypes.c_uint32,
    'maxPerStageDescriptorInlineUniformBlocks': ctypes.c_uint32,
    'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks': ctypes.c_uint32,
    'maxDescriptorSetInlineUniformBlocks': ctypes.c_uint32,
    'maxDescriptorSetUpdateAfterBindInlineUniformBlocks': ctypes.c_uint32,
}
