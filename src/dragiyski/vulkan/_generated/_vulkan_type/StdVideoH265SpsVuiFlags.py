import ctypes

class StdVideoH265SpsVuiFlags(ctypes.Structure):
    _fields_ = [
        ('aspect_ratio_info_present_flag', ctypes.c_uint32, 1),
        ('overscan_info_present_flag', ctypes.c_uint32, 1),
        ('overscan_appropriate_flag', ctypes.c_uint32, 1),
        ('video_signal_type_present_flag', ctypes.c_uint32, 1),
        ('video_full_range_flag', ctypes.c_uint32, 1),
        ('colour_description_present_flag', ctypes.c_uint32, 1),
        ('chroma_loc_info_present_flag', ctypes.c_uint32, 1),
        ('neutral_chroma_indication_flag', ctypes.c_uint32, 1),
        ('field_seq_flag', ctypes.c_uint32, 1),
        ('frame_field_info_present_flag', ctypes.c_uint32, 1),
        ('default_display_window_flag', ctypes.c_uint32, 1),
        ('vui_timing_info_present_flag', ctypes.c_uint32, 1),
        ('vui_poc_proportional_to_timing_flag', ctypes.c_uint32, 1),
        ('vui_hrd_parameters_present_flag', ctypes.c_uint32, 1),
        ('bitstream_restriction_flag', ctypes.c_uint32, 1),
        ('tiles_fixed_structure_flag', ctypes.c_uint32, 1),
        ('motion_vectors_over_pic_boundaries_flag', ctypes.c_uint32, 1),
        ('restricted_ref_pic_lists_flag', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265SequenceParameterSetVui',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'aspect_ratio_info_present_flag': 'aspect_ratio_info_present_flag',
        'overscan_info_present_flag': 'overscan_info_present_flag',
        'overscan_appropriate_flag': 'overscan_appropriate_flag',
        'video_signal_type_present_flag': 'video_signal_type_present_flag',
        'video_full_range_flag': 'video_full_range_flag',
        'colour_description_present_flag': 'colour_description_present_flag',
        'chroma_loc_info_present_flag': 'chroma_loc_info_present_flag',
        'neutral_chroma_indication_flag': 'neutral_chroma_indication_flag',
        'field_seq_flag': 'field_seq_flag',
        'frame_field_info_present_flag': 'frame_field_info_present_flag',
        'default_display_window_flag': 'default_display_window_flag',
        'vui_timing_info_present_flag': 'vui_timing_info_present_flag',
        'vui_poc_proportional_to_timing_flag': 'vui_poc_proportional_to_timing_flag',
        'vui_hrd_parameters_present_flag': 'vui_hrd_parameters_present_flag',
        'bitstream_restriction_flag': 'bitstream_restriction_flag',
        'tiles_fixed_structure_flag': 'tiles_fixed_structure_flag',
        'motion_vectors_over_pic_boundaries_flag': 'motion_vectors_over_pic_boundaries_flag',
        'restricted_ref_pic_lists_flag': 'restricted_ref_pic_lists_flag',
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

StdVideoH265SpsVuiFlags._type_ = {
    'aspect_ratio_info_present_flag': ctypes.c_uint32,
    'overscan_info_present_flag': ctypes.c_uint32,
    'overscan_appropriate_flag': ctypes.c_uint32,
    'video_signal_type_present_flag': ctypes.c_uint32,
    'video_full_range_flag': ctypes.c_uint32,
    'colour_description_present_flag': ctypes.c_uint32,
    'chroma_loc_info_present_flag': ctypes.c_uint32,
    'neutral_chroma_indication_flag': ctypes.c_uint32,
    'field_seq_flag': ctypes.c_uint32,
    'frame_field_info_present_flag': ctypes.c_uint32,
    'default_display_window_flag': ctypes.c_uint32,
    'vui_timing_info_present_flag': ctypes.c_uint32,
    'vui_poc_proportional_to_timing_flag': ctypes.c_uint32,
    'vui_hrd_parameters_present_flag': ctypes.c_uint32,
    'bitstream_restriction_flag': ctypes.c_uint32,
    'tiles_fixed_structure_flag': ctypes.c_uint32,
    'motion_vectors_over_pic_boundaries_flag': ctypes.c_uint32,
    'restricted_ref_pic_lists_flag': ctypes.c_uint32,
}
