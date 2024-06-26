import ctypes

class VkIndirectCommandsLayoutCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkIndirectCommandsLayoutTokenNV',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateIndirectCommandsLayoutNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pipelineBindPoint': 'pipeline_bind_point',
        'tokenCount': 'token_count',
        'pTokens': 'tokens',
        'streamCount': 'stream_count',
        'pStreamStrides': 'stream_strides',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkIndirectCommandsLayoutUsageFlagsNV',
        'pipelineBindPoint': 'VkPipelineBindPoint',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkIndirectCommandsLayoutTokenNV import VkIndirectCommandsLayoutTokenNV

VkIndirectCommandsLayoutCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('tokenCount', ctypes.c_uint32),
    ('pTokens', ctypes.POINTER(VkIndirectCommandsLayoutTokenNV)),
    ('streamCount', ctypes.c_uint32),
    ('pStreamStrides', ctypes.POINTER(ctypes.c_uint32)),
]

VkIndirectCommandsLayoutCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pipelineBindPoint': ctypes.c_int,
    'tokenCount': ctypes.c_uint32,
    'pTokens': ctypes.POINTER(VkIndirectCommandsLayoutTokenNV),
    'streamCount': ctypes.c_uint32,
    'pStreamStrides': ctypes.POINTER(ctypes.c_uint32),
}
