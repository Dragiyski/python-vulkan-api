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

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265HrdParameters',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'nal_hrd_parameters_present_flag': 'nal_hrd_parameters_present_flag',
        'vcl_hrd_parameters_present_flag': 'vcl_hrd_parameters_present_flag',
        'sub_pic_hrd_params_present_flag': 'sub_pic_hrd_params_present_flag',
        'sub_pic_cpb_params_in_pic_timing_sei_flag': 'sub_pic_cpb_params_in_pic_timing_sei_flag',
        'fixed_pic_rate_general_flag': 'fixed_pic_rate_general_flag',
        'fixed_pic_rate_within_cvs_flag': 'fixed_pic_rate_within_cvs_flag',
        'low_delay_hrd_flag': 'low_delay_hrd_flag',
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

StdVideoH265HrdFlags._type_ = {
    'nal_hrd_parameters_present_flag': ctypes.c_uint32,
    'vcl_hrd_parameters_present_flag': ctypes.c_uint32,
    'sub_pic_hrd_params_present_flag': ctypes.c_uint32,
    'sub_pic_cpb_params_in_pic_timing_sei_flag': ctypes.c_uint32,
    'fixed_pic_rate_general_flag': ctypes.c_uint32,
    'fixed_pic_rate_within_cvs_flag': ctypes.c_uint32,
    'low_delay_hrd_flag': ctypes.c_uint32,
}
