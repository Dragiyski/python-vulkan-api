import ctypes

class VkBindDescriptorSetsInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('firstSet', ctypes.c_uint32),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pDescriptorSets', ctypes.POINTER(ctypes.c_void_p)),
        ('dynamicOffsetCount', ctypes.c_uint32),
        ('pDynamicOffsets', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineLayoutCreateInfo',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdBindDescriptorSets2KHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stageFlags': 'stage_flags',
        'layout': 'layout',
        'firstSet': 'first_set',
        'descriptorSetCount': 'descriptor_set_count',
        'pDescriptorSets': 'descriptor_sets',
        'dynamicOffsetCount': 'dynamic_offset_count',
        'pDynamicOffsets': 'dynamic_offsets',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance6',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stageFlags': 'VkShaderStageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_BIND_DESCRIPTOR_SETS_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_BIND_DESCRIPTOR_SETS_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkBindDescriptorSetsInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stageFlags': ctypes.c_uint32,
    'layout': ctypes.c_void_p,
    'firstSet': ctypes.c_uint32,
    'descriptorSetCount': ctypes.c_uint32,
    'pDescriptorSets': ctypes.POINTER(ctypes.c_void_p),
    'dynamicOffsetCount': ctypes.c_uint32,
    'pDynamicOffsets': ctypes.POINTER(ctypes.c_uint32),
}
