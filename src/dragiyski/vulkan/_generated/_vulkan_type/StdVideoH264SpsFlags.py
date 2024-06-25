import ctypes

class StdVideoH264SpsFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
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
