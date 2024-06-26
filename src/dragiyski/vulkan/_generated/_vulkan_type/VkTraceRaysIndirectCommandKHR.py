import ctypes

class VkTraceRaysIndirectCommandKHR(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'width': 'width',
        'height': 'height',
        'depth': 'depth',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_ray_tracing_pipeline',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkTraceRaysIndirectCommandKHR._type_ = {
    'width': ctypes.c_uint32,
    'height': ctypes.c_uint32,
    'depth': ctypes.c_uint32,
}
