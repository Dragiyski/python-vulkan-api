import ctypes

class VkSetDescriptorBufferOffsetsInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('firstSet', ctypes.c_uint32),
        ('setCount', ctypes.c_uint32),
        ('pBufferIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pOffsets', ctypes.POINTER(ctypes.c_uint64)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineLayoutCreateInfo',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdSetDescriptorBufferOffsets2EXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stageFlags': 'stage_flags',
        'layout': 'layout',
        'firstSet': 'first_set',
        'setCount': 'set_count',
        'pBufferIndices': 'buffer_indices',
        'pOffsets': 'offsets',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_maintenance6',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'stageFlags': 'VkShaderStageFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SET_DESCRIPTOR_BUFFER_OFFSETS_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SET_DESCRIPTOR_BUFFER_OFFSETS_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkSetDescriptorBufferOffsetsInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stageFlags': ctypes.c_uint32,
    'layout': ctypes.c_void_p,
    'firstSet': ctypes.c_uint32,
    'setCount': ctypes.c_uint32,
    'pBufferIndices': ctypes.POINTER(ctypes.c_uint32),
    'pOffsets': ctypes.POINTER(ctypes.c_uint64),
}
