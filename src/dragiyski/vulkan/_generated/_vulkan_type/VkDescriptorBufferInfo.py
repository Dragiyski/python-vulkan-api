import ctypes

class VkDescriptorBufferInfo(ctypes.Structure):
    _fields_ = [
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkWriteDescriptorSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'buffer': 'buffer',
        'offset': 'offset',
        'range': 'range',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkDescriptorBufferInfo._type_ = {
    'buffer': ctypes.c_void_p,
    'offset': ctypes.c_uint64,
    'range': ctypes.c_uint64,
}
