import ctypes

class VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxGraphicsShaderGroupCount', ctypes.c_uint32),
        ('maxIndirectSequenceCount', ctypes.c_uint32),
        ('maxIndirectCommandsTokenCount', ctypes.c_uint32),
        ('maxIndirectCommandsStreamCount', ctypes.c_uint32),
        ('maxIndirectCommandsTokenOffset', ctypes.c_uint32),
        ('maxIndirectCommandsStreamStride', ctypes.c_uint32),
        ('minSequencesCountBufferOffsetAlignment', ctypes.c_uint32),
        ('minSequencesIndexBufferOffsetAlignment', ctypes.c_uint32),
        ('minIndirectCommandsBufferOffsetAlignment', ctypes.c_uint32),
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
        'maxGraphicsShaderGroupCount': 'max_graphics_shader_group_count',
        'maxIndirectSequenceCount': 'max_indirect_sequence_count',
        'maxIndirectCommandsTokenCount': 'max_indirect_commands_token_count',
        'maxIndirectCommandsStreamCount': 'max_indirect_commands_stream_count',
        'maxIndirectCommandsTokenOffset': 'max_indirect_commands_token_offset',
        'maxIndirectCommandsStreamStride': 'max_indirect_commands_stream_stride',
        'minSequencesCountBufferOffsetAlignment': 'min_sequences_count_buffer_offset_alignment',
        'minSequencesIndexBufferOffsetAlignment': 'min_sequences_index_buffer_offset_alignment',
        'minIndirectCommandsBufferOffsetAlignment': 'min_indirect_commands_buffer_offset_alignment',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxGraphicsShaderGroupCount': ctypes.c_uint32,
    'maxIndirectSequenceCount': ctypes.c_uint32,
    'maxIndirectCommandsTokenCount': ctypes.c_uint32,
    'maxIndirectCommandsStreamCount': ctypes.c_uint32,
    'maxIndirectCommandsTokenOffset': ctypes.c_uint32,
    'maxIndirectCommandsStreamStride': ctypes.c_uint32,
    'minSequencesCountBufferOffsetAlignment': ctypes.c_uint32,
    'minSequencesIndexBufferOffsetAlignment': ctypes.c_uint32,
    'minIndirectCommandsBufferOffsetAlignment': ctypes.c_uint32,
}
