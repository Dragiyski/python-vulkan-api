import ctypes

class VkPerformanceValueDataINTEL(ctypes.Union):
    _fields_ = [
        ('value32', ctypes.c_uint32),
        ('value64', ctypes.c_uint64),
        ('valueFloat', ctypes.c_float),
        ('valueBool', ctypes.c_uint32),
        ('valueString', ctypes.c_char_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPerformanceValueINTEL',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'value32': 'value32',
        'value64': 'value64',
        'valueFloat': 'value_float',
        'valueBool': 'value_bool',
        'valueString': 'value_string',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_INTEL_performance_query',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkPerformanceValueDataINTEL._type_ = {
    'value32': ctypes.c_uint32,
    'value64': ctypes.c_uint64,
    'valueFloat': ctypes.c_float,
    'valueBool': ctypes.c_uint32,
    'valueString': ctypes.c_char_p,
}
