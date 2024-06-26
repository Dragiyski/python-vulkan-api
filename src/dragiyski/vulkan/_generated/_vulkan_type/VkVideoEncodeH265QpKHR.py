import ctypes

class VkVideoEncodeH265QpKHR(ctypes.Structure):
    _fields_ = [
        ('qpI', ctypes.c_int32),
        ('qpP', ctypes.c_int32),
        ('qpB', ctypes.c_int32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkVideoEncodeH265QualityLevelPropertiesKHR',
        'VkVideoEncodeH265RateControlLayerInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'qpI': 'qp_i',
        'qpP': 'qp',
        'qpB': 'qp_b',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeH265QpKHR._type_ = {
    'qpI': ctypes.c_int32,
    'qpP': ctypes.c_int32,
    'qpB': ctypes.c_int32,
}
