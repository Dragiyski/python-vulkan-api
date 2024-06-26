import ctypes

class StdVideoH265ShortTermRefPicSet(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH265ShortTermRefPicSetFlags',
    }
    _included_in_ = {
        'StdVideoEncodeH265PictureInfo',
        'StdVideoH265SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'delta_idx_minus1': 'delta_idx_minus1',
        'use_delta_flag': 'use_delta_flag',
        'abs_delta_rps_minus1': 'abs_delta_rps_minus1',
        'used_by_curr_pic_flag': 'used_by_curr_pic_flag',
        'used_by_curr_pic_s0_flag': 'used_by_curr_pic_s0_flag',
        'used_by_curr_pic_s1_flag': 'used_by_curr_pic_s1_flag',
        'reserved1': 'reserved1',
        'reserved2': 'reserved2',
        'reserved3': 'reserved3',
        'num_negative_pics': 'num_negative_pics',
        'num_positive_pics': 'num_positive_pics',
        'delta_poc_s0_minus1': 'delta_poc_s0_minus1',
        'delta_poc_s1_minus1': 'delta_poc_s1_minus1',
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


from .StdVideoH265ShortTermRefPicSetFlags import StdVideoH265ShortTermRefPicSetFlags

StdVideoH265ShortTermRefPicSet._fields_ = [
    ('flags', StdVideoH265ShortTermRefPicSetFlags),
    ('delta_idx_minus1', ctypes.c_uint32),
    ('use_delta_flag', ctypes.c_uint16),
    ('abs_delta_rps_minus1', ctypes.c_uint16),
    ('used_by_curr_pic_flag', ctypes.c_uint16),
    ('used_by_curr_pic_s0_flag', ctypes.c_uint16),
    ('used_by_curr_pic_s1_flag', ctypes.c_uint16),
    ('reserved1', ctypes.c_uint16),
    ('reserved2', ctypes.c_uint8),
    ('reserved3', ctypes.c_uint8),
    ('num_negative_pics', ctypes.c_uint8),
    ('num_positive_pics', ctypes.c_uint8),
    ('delta_poc_s0_minus1', ctypes.ARRAY(ctypes.c_uint16, 16)),
    ('delta_poc_s1_minus1', ctypes.ARRAY(ctypes.c_uint16, 16)),
]

StdVideoH265ShortTermRefPicSet._type_ = {
    'flags': StdVideoH265ShortTermRefPicSetFlags,
    'delta_idx_minus1': ctypes.c_uint32,
    'use_delta_flag': ctypes.c_uint16,
    'abs_delta_rps_minus1': ctypes.c_uint16,
    'used_by_curr_pic_flag': ctypes.c_uint16,
    'used_by_curr_pic_s0_flag': ctypes.c_uint16,
    'used_by_curr_pic_s1_flag': ctypes.c_uint16,
    'reserved1': ctypes.c_uint16,
    'reserved2': ctypes.c_uint8,
    'reserved3': ctypes.c_uint8,
    'num_negative_pics': ctypes.c_uint8,
    'num_positive_pics': ctypes.c_uint8,
    'delta_poc_s0_minus1': ctypes.ARRAY(ctypes.c_uint16, 16),
    'delta_poc_s1_minus1': ctypes.ARRAY(ctypes.c_uint16, 16),
}
