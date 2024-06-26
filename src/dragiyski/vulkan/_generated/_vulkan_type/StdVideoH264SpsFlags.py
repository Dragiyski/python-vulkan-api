import ctypes

class StdVideoH264SpsFlags(ctypes.Structure):
    _fields_ = [
        ('constraint_set0_flag', ctypes.c_uint32, 1),
        ('constraint_set1_flag', ctypes.c_uint32, 1),
        ('constraint_set2_flag', ctypes.c_uint32, 1),
        ('constraint_set3_flag', ctypes.c_uint32, 1),
        ('constraint_set4_flag', ctypes.c_uint32, 1),
        ('constraint_set5_flag', ctypes.c_uint32, 1),
        ('direct_8x8_inference_flag', ctypes.c_uint32, 1),
        ('mb_adaptive_frame_field_flag', ctypes.c_uint32, 1),
        ('frame_mbs_only_flag', ctypes.c_uint32, 1),
        ('delta_pic_order_always_zero_flag', ctypes.c_uint32, 1),
        ('separate_colour_plane_flag', ctypes.c_uint32, 1),
        ('gaps_in_frame_num_value_allowed_flag', ctypes.c_uint32, 1),
        ('qpprime_y_zero_transform_bypass_flag', ctypes.c_uint32, 1),
        ('frame_cropping_flag', ctypes.c_uint32, 1),
        ('seq_scaling_matrix_present_flag', ctypes.c_uint32, 1),
        ('vui_parameters_present_flag', ctypes.c_uint32, 1),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH264SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'constraint_set0_flag': 'constraint_set0_flag',
        'constraint_set1_flag': 'constraint_set1_flag',
        'constraint_set2_flag': 'constraint_set2_flag',
        'constraint_set3_flag': 'constraint_set3_flag',
        'constraint_set4_flag': 'constraint_set4_flag',
        'constraint_set5_flag': 'constraint_set5_flag',
        'direct_8x8_inference_flag': 'direct_8x8_inference_flag',
        'mb_adaptive_frame_field_flag': 'mb_adaptive_frame_field_flag',
        'frame_mbs_only_flag': 'frame_mbs_only_flag',
        'delta_pic_order_always_zero_flag': 'delta_pic_order_always_zero_flag',
        'separate_colour_plane_flag': 'separate_colour_plane_flag',
        'gaps_in_frame_num_value_allowed_flag': 'gaps_in_frame_num_value_allowed_flag',
        'qpprime_y_zero_transform_bypass_flag': 'qpprime_y_zero_transform_bypass_flag',
        'frame_cropping_flag': 'frame_cropping_flag',
        'seq_scaling_matrix_present_flag': 'seq_scaling_matrix_present_flag',
        'vui_parameters_present_flag': 'vui_parameters_present_flag',
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

StdVideoH264SpsFlags._type_ = {
    'constraint_set0_flag': ctypes.c_uint32,
    'constraint_set1_flag': ctypes.c_uint32,
    'constraint_set2_flag': ctypes.c_uint32,
    'constraint_set3_flag': ctypes.c_uint32,
    'constraint_set4_flag': ctypes.c_uint32,
    'constraint_set5_flag': ctypes.c_uint32,
    'direct_8x8_inference_flag': ctypes.c_uint32,
    'mb_adaptive_frame_field_flag': ctypes.c_uint32,
    'frame_mbs_only_flag': ctypes.c_uint32,
    'delta_pic_order_always_zero_flag': ctypes.c_uint32,
    'separate_colour_plane_flag': ctypes.c_uint32,
    'gaps_in_frame_num_value_allowed_flag': ctypes.c_uint32,
    'qpprime_y_zero_transform_bypass_flag': ctypes.c_uint32,
    'frame_cropping_flag': ctypes.c_uint32,
    'seq_scaling_matrix_present_flag': ctypes.c_uint32,
    'vui_parameters_present_flag': ctypes.c_uint32,
}
