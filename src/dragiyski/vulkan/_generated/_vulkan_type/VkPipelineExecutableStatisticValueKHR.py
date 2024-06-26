import ctypes

class VkPipelineExecutableStatisticValueKHR(ctypes.Union):
    _fields_ = [
        ('b32', ctypes.c_uint32),
        ('i64', ctypes.c_int64),
        ('u64', ctypes.c_uint64),
        ('f64', ctypes.c_double),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPipelineExecutableStatisticKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'b32': 'b32',
        'i64': 'i64',
        'u64': 'u64',
        'f64': 'f64',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_pipeline_executable_properties',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineExecutableStatisticValueKHR._type_ = {
    'b32': ctypes.c_uint32,
    'i64': ctypes.c_int64,
    'u64': ctypes.c_uint64,
    'f64': ctypes.c_double,
}
