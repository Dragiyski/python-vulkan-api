import ctypes

class VkDescriptorPoolSize(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkDescriptorPoolCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'type': 'type',
        'descriptorCount': 'descriptor_count',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'type': 'VkDescriptorType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorPoolSize._type_ = {
    'type': ctypes.c_int,
    'descriptorCount': ctypes.c_uint32,
}
