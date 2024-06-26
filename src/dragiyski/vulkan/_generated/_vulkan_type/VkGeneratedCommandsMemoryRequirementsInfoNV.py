import ctypes

class VkGeneratedCommandsMemoryRequirementsInfoNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineBindPoint', ctypes.c_int),
        ('pipeline', ctypes.c_void_p),
        ('indirectCommandsLayout', ctypes.c_void_p),
        ('maxSequencesCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetGeneratedCommandsMemoryRequirementsNV',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pipelineBindPoint': 'pipeline_bind_point',
        'pipeline': 'pipeline',
        'indirectCommandsLayout': 'indirect_commands_layout',
        'maxSequencesCount': 'max_sequences_count',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pipelineBindPoint': 'VkPipelineBindPoint',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)

VkGeneratedCommandsMemoryRequirementsInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pipelineBindPoint': ctypes.c_int,
    'pipeline': ctypes.c_void_p,
    'indirectCommandsLayout': ctypes.c_void_p,
    'maxSequencesCount': ctypes.c_uint32,
}
