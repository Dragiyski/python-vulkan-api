import ctypes, sys

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

sys.modules[__name__] = StdVideoH264SpsVuiFlags
