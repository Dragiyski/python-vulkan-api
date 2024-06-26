import ctypes

class VkRefreshObjectKHR(ctypes.Structure):
    _fields_ = [
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'objectType': 'object_type',
        'objectHandle': 'object_handle',
        'flags': 'flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = set()
    _vk_enum_ = {
        'objectType': 'VkObjectType',
        'flags': 'VkRefreshObjectFlagsKHR',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkRefreshObjectKHR._type_ = {
    'objectType': ctypes.c_int,
    'objectHandle': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
