import ctypes

class VkSpecializationMapEntry(ctypes.Structure):
    _fields_ = [
        ('constantID', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_size_t),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkSpecializationInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'constantID': 'constant_id',
        'offset': 'offset',
        'size': 'size',
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

VkSpecializationMapEntry._type_ = {
    'constantID': ctypes.c_uint32,
    'offset': ctypes.c_uint32,
    'size': ctypes.c_size_t,
}
