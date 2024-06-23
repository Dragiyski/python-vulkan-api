import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH264SequenceParameterSetVui',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'aspect_ratio_info_present_flag': {'python_name': ['aspect', 'ratio', 'info', 'present', 'flag']},
        'overscan_info_present_flag': {'python_name': ['overscan', 'info', 'present', 'flag']},
        'overscan_appropriate_flag': {'python_name': ['overscan', 'appropriate', 'flag']},
        'video_signal_type_present_flag': {'python_name': ['video', 'signal', 'type', 'present', 'flag']},
        'video_full_range_flag': {'python_name': ['video', 'full', 'range', 'flag']},
        'color_description_present_flag': {'python_name': ['color', 'description', 'present', 'flag']},
        'chroma_loc_info_present_flag': {'python_name': ['chroma', 'loc', 'info', 'present', 'flag']},
        'timing_info_present_flag': {'python_name': ['timing', 'info', 'present', 'flag']},
        'fixed_frame_rate_flag': {'python_name': ['fixed', 'frame', 'rate', 'flag']},
        'bitstream_restriction_flag': {'python_name': ['bitstream', 'restriction', 'flag']},
        'nal_hrd_parameters_present_flag': {'python_name': ['nal', 'hrd', 'parameters', 'present', 'flag']},
        'vcl_hrd_parameters_present_flag': {'python_name': ['vcl', 'hrd', 'parameters', 'present', 'flag']},
    }
}
