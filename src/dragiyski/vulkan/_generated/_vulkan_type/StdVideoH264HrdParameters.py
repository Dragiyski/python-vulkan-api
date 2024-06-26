import ctypes

class StdVideoH264HrdParameters(ctypes.Structure):
    _fields_ = [
        ('cpb_cnt_minus1', ctypes.c_uint8),
        ('bit_rate_scale', ctypes.c_uint8),
        ('cpb_size_scale', ctypes.c_uint8),
        ('reserved1', ctypes.c_uint8),
        ('bit_rate_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cbr_flag', ctypes.ARRAY(ctypes.c_uint8, 32)),
        ('initial_cpb_removal_delay_length_minus1', ctypes.c_uint32),
        ('cpb_removal_delay_length_minus1', ctypes.c_uint32),
        ('dpb_output_delay_length_minus1', ctypes.c_uint32),
        ('time_offset_length', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH264SequenceParameterSetVui',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'cpb_cnt_minus1': 'cpb_cnt_minus1',
        'bit_rate_scale': 'bit_rate_scale',
        'cpb_size_scale': 'cpb_size_scale',
        'reserved1': 'reserved1',
        'bit_rate_value_minus1': 'bit_rate_value_minus1',
        'cpb_size_value_minus1': 'cpb_size_value_minus1',
        'cbr_flag': 'cbr_flag',
        'initial_cpb_removal_delay_length_minus1': 'initial_cpb_removal_delay_length_minus1',
        'cpb_removal_delay_length_minus1': 'cpb_removal_delay_length_minus1',
        'dpb_output_delay_length_minus1': 'dpb_output_delay_length_minus1',
        'time_offset_length': 'time_offset_length',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h264std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoH264HrdParameters._type_ = {
    'cpb_cnt_minus1': ctypes.c_uint8,
    'bit_rate_scale': ctypes.c_uint8,
    'cpb_size_scale': ctypes.c_uint8,
    'reserved1': ctypes.c_uint8,
    'bit_rate_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cpb_size_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
    'cbr_flag': ctypes.ARRAY(ctypes.c_uint8, 32),
    'initial_cpb_removal_delay_length_minus1': ctypes.c_uint32,
    'cpb_removal_delay_length_minus1': ctypes.c_uint32,
    'dpb_output_delay_length_minus1': ctypes.c_uint32,
    'time_offset_length': ctypes.c_uint32,
}
