import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265SequenceParameterSetVui',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'aspect_ratio_info_present_flag': {'python_name': ['aspect', 'ratio', 'info', 'present', 'flag']},
        'overscan_info_present_flag': {'python_name': ['overscan', 'info', 'present', 'flag']},
        'overscan_appropriate_flag': {'python_name': ['overscan', 'appropriate', 'flag']},
        'video_signal_type_present_flag': {'python_name': ['video', 'signal', 'type', 'present', 'flag']},
        'video_full_range_flag': {'python_name': ['video', 'full', 'range', 'flag']},
        'colour_description_present_flag': {'python_name': ['colour', 'description', 'present', 'flag']},
        'chroma_loc_info_present_flag': {'python_name': ['chroma', 'loc', 'info', 'present', 'flag']},
        'neutral_chroma_indication_flag': {'python_name': ['neutral', 'chroma', 'indication', 'flag']},
        'field_seq_flag': {'python_name': ['field', 'seq', 'flag']},
        'frame_field_info_present_flag': {'python_name': ['frame', 'field', 'info', 'present', 'flag']},
        'default_display_window_flag': {'python_name': ['default', 'display', 'window', 'flag']},
        'vui_timing_info_present_flag': {'python_name': ['vui', 'timing', 'info', 'present', 'flag']},
        'vui_poc_proportional_to_timing_flag': {'python_name': ['vui', 'poc', 'proportional', 'to', 'timing', 'flag']},
        'vui_hrd_parameters_present_flag': {'python_name': ['vui', 'hrd', 'parameters', 'present', 'flag']},
        'bitstream_restriction_flag': {'python_name': ['bitstream', 'restriction', 'flag']},
        'tiles_fixed_structure_flag': {'python_name': ['tiles', 'fixed', 'structure', 'flag']},
        'motion_vectors_over_pic_boundaries_flag': {'python_name': ['motion', 'vectors', 'over', 'pic', 'boundaries', 'flag']},
        'restricted_ref_pic_lists_flag': {'python_name': ['restricted', 'ref', 'pic', 'lists', 'flag']},
    }
}
