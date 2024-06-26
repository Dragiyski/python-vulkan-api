import ctypes

class StdVideoEncodeH265LongTermRefPics(ctypes.Structure):
    _fields_ = [
        ('num_long_term_sps', ctypes.c_uint8),
        ('num_long_term_pics', ctypes.c_uint8),
        ('lt_idx_sps', ctypes.ARRAY(ctypes.c_uint8, 32)),
        ('poc_lsb_lt', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('used_by_curr_pic_lt_flag', ctypes.c_uint16),
        ('delta_poc_msb_present_flag', ctypes.ARRAY(ctypes.c_uint8, 48)),
        ('delta_poc_msb_cycle_lt', ctypes.ARRAY(ctypes.c_uint8, 48)),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoEncodeH265PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'num_long_term_sps': 'num_long_term_sps',
        'num_long_term_pics': 'num_long_term_pics',
        'lt_idx_sps': 'lt_idx_sps',
        'poc_lsb_lt': 'poc_lsb_lt',
        'used_by_curr_pic_lt_flag': 'used_by_curr_pic_lt_flag',
        'delta_poc_msb_present_flag': 'delta_poc_msb_present_flag',
        'delta_poc_msb_cycle_lt': 'delta_poc_msb_cycle_lt',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_encode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH265LongTermRefPics._type_ = {
    'num_long_term_sps': ctypes.c_uint8,
    'num_long_term_pics': ctypes.c_uint8,
    'lt_idx_sps': ctypes.ARRAY(ctypes.c_uint8, 32),
    'poc_lsb_lt': ctypes.ARRAY(ctypes.c_uint8, 16),
    'used_by_curr_pic_lt_flag': ctypes.c_uint16,
    'delta_poc_msb_present_flag': ctypes.ARRAY(ctypes.c_uint8, 48),
    'delta_poc_msb_cycle_lt': ctypes.ARRAY(ctypes.c_uint8, 48),
}
