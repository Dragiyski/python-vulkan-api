import ctypes

class VkDescriptorSetLayoutBinding(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
        ('stageFlags', ctypes.c_uint32),
        ('pImmutableSamplers', ctypes.POINTER(ctypes.c_void_p)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDescriptorSetLayoutCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'binding': 'binding',
        'descriptorType': 'descriptor_type',
        'descriptorCount': 'descriptor_count',
        'stageFlags': 'stage_flags',
        'pImmutableSamplers': 'immutable_samplers',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'descriptorType': 'VkDescriptorType',
        'stageFlags': 'VkShaderStageFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorSetLayoutBinding._type_ = {
    'binding': ctypes.c_uint32,
    'descriptorType': ctypes.c_int,
    'descriptorCount': ctypes.c_uint32,
    'stageFlags': ctypes.c_uint32,
    'pImmutableSamplers': ctypes.POINTER(ctypes.c_void_p),
}
