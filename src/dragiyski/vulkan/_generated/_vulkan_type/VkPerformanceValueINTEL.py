import ctypes

class VkPerformanceValueINTEL(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkPerformanceValueDataINTEL',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetPerformanceParameterINTEL',
    }
    _python_name_ = {
        'type': 'type',
        'data': 'data',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_INTEL_performance_query',
    }
    _vk_enum_ = {
        'type': 'VkPerformanceValueTypeINTEL',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPerformanceValueDataINTEL import VkPerformanceValueDataINTEL

VkPerformanceValueINTEL._fields_ = [
    ('type', ctypes.c_int),
    ('data', VkPerformanceValueDataINTEL),
]

VkPerformanceValueINTEL._type_ = {
    'type': ctypes.c_int,
    'data': VkPerformanceValueDataINTEL,
}
