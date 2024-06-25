import ctypes

class StdVideoH265HrdFlags(ctypes.Structure):
    _fields_ = [
        ('nal_hrd_parameters_present_flag', ctypes.c_uint32, 1),
        ('vcl_hrd_parameters_present_flag', ctypes.c_uint32, 1),
        ('sub_pic_hrd_params_present_flag', ctypes.c_uint32, 1),
        ('sub_pic_cpb_params_in_pic_timing_sei_flag', ctypes.c_uint32, 1),
        ('fixed_pic_rate_general_flag', ctypes.c_uint32, 8),
        ('fixed_pic_rate_within_cvs_flag', ctypes.c_uint32, 8),
        ('low_delay_hrd_flag', ctypes.c_uint32, 8),
    ]

StdVideoH265HrdFlags._type_ = {
    'nal_hrd_parameters_present_flag': ctypes.c_uint32,
    'vcl_hrd_parameters_present_flag': ctypes.c_uint32,
    'sub_pic_hrd_params_present_flag': ctypes.c_uint32,
    'sub_pic_cpb_params_in_pic_timing_sei_flag': ctypes.c_uint32,
    'fixed_pic_rate_general_flag': ctypes.c_uint32,
    'fixed_pic_rate_within_cvs_flag': ctypes.c_uint32,
    'low_delay_hrd_flag': ctypes.c_uint32,
}
