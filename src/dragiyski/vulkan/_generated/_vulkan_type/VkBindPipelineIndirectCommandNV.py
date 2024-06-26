import ctypes

class VkBindPipelineIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('pipelineAddress', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'pipelineAddress': 'pipeline_address',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands_compute',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkBindPipelineIndirectCommandNV._type_ = {
    'pipelineAddress': ctypes.c_uint64,
}
