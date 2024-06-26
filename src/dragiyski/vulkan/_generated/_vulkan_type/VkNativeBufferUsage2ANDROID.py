import ctypes

class VkNativeBufferUsage2ANDROID(ctypes.Structure):
    _fields_ = [
        ('consumer', ctypes.c_uint64),
        ('producer', ctypes.c_uint64),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'consumer': 'consumer',
        'producer': 'producer',
    }
    _vk_versions_ = set()
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkNativeBufferUsage2ANDROID._type_ = {
    'consumer': ctypes.c_uint64,
    'producer': ctypes.c_uint64,
}
