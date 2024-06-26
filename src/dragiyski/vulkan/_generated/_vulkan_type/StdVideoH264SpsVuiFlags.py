import ctypes

class StdVideoH264SpsVuiFlags(ctypes.Structure):
    _fields_ = [
        ('aspect_ratio_info_present_flag', ctypes.c_uint32, 1),
        ('overscan_info_present_flag', ctypes.c_uint32, 1),
        ('overscan_appropriate_flag', ctypes.c_uint32, 1),
        ('video_signal_type_present_flag', ctypes.c_uint32, 1),
        ('video_full_range_flag', ctypes.c_uint32, 1),
        ('color_description_present_flag', ctypes.c_uint32, 1),
        ('chroma_loc_info_present_flag', ctypes.c_uint32, 1),
        ('timing_info_present_flag', ctypes.c_uint32, 1),
        ('fixed_frame_rate_flag', ctypes.c_uint32, 1),
        ('bitstream_restriction_flag', ctypes.c_uint32, 1),
        ('nal_hrd_parameters_present_flag', ctypes.c_uint32, 1),
        ('vcl_hrd_parameters_present_flag', ctypes.c_uint32, 1),
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
        'aspect_ratio_info_present_flag': 'aspect_ratio_info_present_flag',
        'overscan_info_present_flag': 'overscan_info_present_flag',
        'overscan_appropriate_flag': 'overscan_appropriate_flag',
        'video_signal_type_present_flag': 'video_signal_type_present_flag',
        'video_full_range_flag': 'video_full_range_flag',
        'color_description_present_flag': 'color_description_present_flag',
        'chroma_loc_info_present_flag': 'chroma_loc_info_present_flag',
        'timing_info_present_flag': 'timing_info_present_flag',
        'fixed_frame_rate_flag': 'fixed_frame_rate_flag',
        'bitstream_restriction_flag': 'bitstream_restriction_flag',
        'nal_hrd_parameters_present_flag': 'nal_hrd_parameters_present_flag',
        'vcl_hrd_parameters_present_flag': 'vcl_hrd_parameters_present_flag',
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

StdVideoH264SpsVuiFlags._type_ = {
    'aspect_ratio_info_present_flag': ctypes.c_uint32,
    'overscan_info_present_flag': ctypes.c_uint32,
    'overscan_appropriate_flag': ctypes.c_uint32,
    'video_signal_type_present_flag': ctypes.c_uint32,
    'video_full_range_flag': ctypes.c_uint32,
    'color_description_present_flag': ctypes.c_uint32,
    'chroma_loc_info_present_flag': ctypes.c_uint32,
    'timing_info_present_flag': ctypes.c_uint32,
    'fixed_frame_rate_flag': ctypes.c_uint32,
    'bitstream_restriction_flag': ctypes.c_uint32,
    'nal_hrd_parameters_present_flag': ctypes.c_uint32,
    'vcl_hrd_parameters_present_flag': ctypes.c_uint32,
}
