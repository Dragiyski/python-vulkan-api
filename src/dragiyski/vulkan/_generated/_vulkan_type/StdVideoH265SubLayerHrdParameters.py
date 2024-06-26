import ctypes

class StdVideoH265SubLayerHrdParameters(ctypes.Structure):
    _fields_ = [
        ('bit_rate_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_du_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('bit_rate_du_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cbr_flag', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265HrdParameters',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'bit_rate_value_minus1': 'bit_rate_value_minus1',
        'cpb_size_value_minus1': 'cpb_size_value_minus1',
        'cpb_size_du_value_minus1': 'cpb_size_du_value_minus1',
        'bit_rate_du_value_minus1': 'bit_rate_du_value_minus1',
        'cbr_flag': 'cbr_flag',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoH265SubLayerHrdParameters._type_ = {
    'bit_rate_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cpb_size_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cpb_size_du_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'bit_rate_du_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cbr_flag': ctypes.c_uint32,
}
