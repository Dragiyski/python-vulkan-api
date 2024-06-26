import ctypes

class VkGeneratedCommandsInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkIndirectCommandsStreamNV',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCmdExecuteGeneratedCommandsNV',
        'vkCmdPreprocessGeneratedCommandsNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pipelineBindPoint': 'pipeline_bind_point',
        'pipeline': 'pipeline',
        'indirectCommandsLayout': 'indirect_commands_layout',
        'streamCount': 'stream_count',
        'pStreams': 'streams',
        'sequencesCount': 'sequences_count',
        'preprocessBuffer': 'preprocess_buffer',
        'preprocessOffset': 'preprocess_offset',
        'preprocessSize': 'preprocess_size',
        'sequencesCountBuffer': 'sequences_count_buffer',
        'sequencesCountOffset': 'sequences_count_offset',
        'sequencesIndexBuffer': 'sequences_index_buffer',
        'sequencesIndexOffset': 'sequences_index_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pipelineBindPoint': 'VkPipelineBindPoint',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkIndirectCommandsStreamNV import VkIndirectCommandsStreamNV

VkGeneratedCommandsInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pipelineBindPoint', ctypes.c_int),
    ('pipeline', ctypes.c_void_p),
    ('indirectCommandsLayout', ctypes.c_void_p),
    ('streamCount', ctypes.c_uint32),
    ('pStreams', ctypes.POINTER(VkIndirectCommandsStreamNV)),
    ('sequencesCount', ctypes.c_uint32),
    ('preprocessBuffer', ctypes.c_void_p),
    ('preprocessOffset', ctypes.c_uint64),
    ('preprocessSize', ctypes.c_uint64),
    ('sequencesCountBuffer', ctypes.c_void_p),
    ('sequencesCountOffset', ctypes.c_uint64),
    ('sequencesIndexBuffer', ctypes.c_void_p),
    ('sequencesIndexOffset', ctypes.c_uint64),
]

VkGeneratedCommandsInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineBindPoint': ctypes.c_int,
    'pipeline': ctypes.c_void_p,
    'indirectCommandsLayout': ctypes.c_void_p,
    'streamCount': ctypes.c_uint32,
    'pStreams': ctypes.POINTER(VkIndirectCommandsStreamNV),
    'sequencesCount': ctypes.c_uint32,
    'preprocessBuffer': ctypes.c_void_p,
    'preprocessOffset': ctypes.c_uint64,
    'preprocessSize': ctypes.c_uint64,
    'sequencesCountBuffer': ctypes.c_void_p,
    'sequencesCountOffset': ctypes.c_uint64,
    'sequencesIndexBuffer': ctypes.c_void_p,
    'sequencesIndexOffset': ctypes.c_uint64,
}
