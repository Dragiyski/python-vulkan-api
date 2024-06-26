import ctypes

class VkPushConstantRange(ctypes.Structure):
    _fields_ = [
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineLayoutCreateInfo',
        'VkShaderCreateInfoEXT',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'stageFlags': 'stage_flags',
        'offset': 'offset',
        'size': 'size',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'stageFlags': 'VkShaderStageFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPushConstantRange._type_ = {
    'stageFlags': ctypes.c_uint32,
    'offset': ctypes.c_uint32,
    'size': ctypes.c_uint32,
}
