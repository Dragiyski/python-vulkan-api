import ctypes

class StdVideoEncodeH265PictureInfoFlags(ctypes.Structure):
    _fields_ = [
        ('is_reference', ctypes.c_uint32, 1),
        ('IrapPicFlag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('discardable_flag', ctypes.c_uint32, 1),
        ('cross_layer_bla_flag', ctypes.c_uint32, 1),
        ('pic_output_flag', ctypes.c_uint32, 1),
        ('no_output_of_prior_pics_flag', ctypes.c_uint32, 1),
        ('short_term_ref_pic_set_sps_flag', ctypes.c_uint32, 1),
        ('slice_temporal_mvp_enabled_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 23),
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
        'is_reference': 'is_reference',
        'IrapPicFlag': 'irap_pic_flag',
        'used_for_long_term_reference': 'used_for_long_term_reference',
        'discardable_flag': 'discardable_flag',
        'cross_layer_bla_flag': 'cross_layer_bla_flag',
        'pic_output_flag': 'pic_output_flag',
        'no_output_of_prior_pics_flag': 'no_output_of_prior_pics_flag',
        'short_term_ref_pic_set_sps_flag': 'short_term_ref_pic_set_sps_flag',
        'slice_temporal_mvp_enabled_flag': 'slice_temporal_mvp_enabled_flag',
        'reserved': 'reserved',
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

StdVideoEncodeH265PictureInfoFlags._type_ = {
    'is_reference': ctypes.c_uint32,
    'IrapPicFlag': ctypes.c_uint32,
    'used_for_long_term_reference': ctypes.c_uint32,
    'discardable_flag': ctypes.c_uint32,
    'cross_layer_bla_flag': ctypes.c_uint32,
    'pic_output_flag': ctypes.c_uint32,
    'no_output_of_prior_pics_flag': ctypes.c_uint32,
    'short_term_ref_pic_set_sps_flag': ctypes.c_uint32,
    'slice_temporal_mvp_enabled_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
