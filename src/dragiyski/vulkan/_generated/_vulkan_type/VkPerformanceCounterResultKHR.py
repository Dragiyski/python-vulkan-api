import ctypes

class VkPerformanceCounterResultKHR(ctypes.Union):
    _fields_ = [
        ('int32', ctypes.c_int32),
        ('int64', ctypes.c_int64),
        ('uint32', ctypes.c_uint32),
        ('uint64', ctypes.c_uint64),
        ('float32', ctypes.c_float),
        ('float64', ctypes.c_double),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'int32': 'int32',
        'int64': 'int64',
        'uint32': 'uint32',
        'uint64': 'uint64',
        'float32': 'float32',
        'float64': 'float64',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_performance_query',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPerformanceCounterResultKHR._type_ = {
    'int32': ctypes.c_int32,
    'int64': ctypes.c_int64,
    'uint32': ctypes.c_uint32,
    'uint64': ctypes.c_uint64,
    'float32': ctypes.c_float,
    'float64': ctypes.c_double,
}
