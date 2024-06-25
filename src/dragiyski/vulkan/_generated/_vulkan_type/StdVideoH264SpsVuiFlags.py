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
