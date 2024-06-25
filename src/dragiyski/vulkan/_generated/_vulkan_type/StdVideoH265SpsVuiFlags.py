import ctypes

class StdVideoH265SpsVuiFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
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
