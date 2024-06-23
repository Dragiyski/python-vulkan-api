import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH264SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'constraint_set0_flag': {'python_name': ['constraint', 'set0', 'flag']},
        'constraint_set1_flag': {'python_name': ['constraint', 'set1', 'flag']},
        'constraint_set2_flag': {'python_name': ['constraint', 'set2', 'flag']},
        'constraint_set3_flag': {'python_name': ['constraint', 'set3', 'flag']},
        'constraint_set4_flag': {'python_name': ['constraint', 'set4', 'flag']},
        'constraint_set5_flag': {'python_name': ['constraint', 'set5', 'flag']},
        'direct_8x8_inference_flag': {'python_name': ['direct', '8x8', 'inference', 'flag']},
        'mb_adaptive_frame_field_flag': {'python_name': ['mb', 'adaptive', 'frame', 'field', 'flag']},
        'frame_mbs_only_flag': {'python_name': ['frame', 'mbs', 'only', 'flag']},
        'delta_pic_order_always_zero_flag': {'python_name': ['delta', 'pic', 'order', 'always', 'zero', 'flag']},
        'separate_colour_plane_flag': {'python_name': ['separate', 'colour', 'plane', 'flag']},
        'gaps_in_frame_num_value_allowed_flag': {'python_name': ['gaps', 'in', 'frame', 'num', 'value', 'allowed', 'flag']},
        'qpprime_y_zero_transform_bypass_flag': {'python_name': ['qpprime', 'y', 'zero', 'transform', 'bypass', 'flag']},
        'frame_cropping_flag': {'python_name': ['frame', 'cropping', 'flag']},
        'seq_scaling_matrix_present_flag': {'python_name': ['seq', 'scaling', 'matrix', 'present', 'flag']},
        'vui_parameters_present_flag': {'python_name': ['vui', 'parameters', 'present', 'flag']},
    }
}
