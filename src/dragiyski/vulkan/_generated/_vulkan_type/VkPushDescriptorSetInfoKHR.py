import ctypes

class VkPushDescriptorSetInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineLayoutCreateInfo',
    }
    _includes_ = {
        'VkWriteDescriptorSet',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdPushDescriptorSet2KHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stageFlags': 'stage_flags',
        'layout': 'layout',
        'set': 'set',
        'descriptorWriteCount': 'descriptor_write_count',
        'pDescriptorWrites': 'descriptor_writes',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance6',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stageFlags': 'VkShaderStageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkWriteDescriptorSet import VkWriteDescriptorSet

VkPushDescriptorSetInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stageFlags', ctypes.c_uint32),
    ('layout', ctypes.c_void_p),
    ('set', ctypes.c_uint32),
    ('descriptorWriteCount', ctypes.c_uint32),
    ('pDescriptorWrites', ctypes.POINTER(VkWriteDescriptorSet)),
]

VkPushDescriptorSetInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stageFlags': ctypes.c_uint32,
    'layout': ctypes.c_void_p,
    'set': ctypes.c_uint32,
    'descriptorWriteCount': ctypes.c_uint32,
    'pDescriptorWrites': ctypes.POINTER(VkWriteDescriptorSet),
}
