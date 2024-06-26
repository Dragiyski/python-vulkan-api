import ctypes

class VkBindVertexBufferIndirectCommandNV(ctypes.Structure):
    _fields_ = [
        ('bufferAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'bufferAddress': 'buffer_address',
        'size': 'size',
        'stride': 'stride',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkBindVertexBufferIndirectCommandNV._type_ = {
    'bufferAddress': ctypes.c_uint64,
    'size': ctypes.c_uint32,
    'stride': ctypes.c_uint32,
}
