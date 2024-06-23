import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('transform_8x8_mode_flag', ctypes.c_uint32, 1),
        ('redundant_pic_cnt_present_flag', ctypes.c_uint32, 1),
        ('constrained_intra_pred_flag', ctypes.c_uint32, 1),
        ('deblocking_filter_control_present_flag', ctypes.c_uint32, 1),
        ('weighted_pred_flag', ctypes.c_uint32, 1),
        ('bottom_field_pic_order_in_frame_present_flag', ctypes.c_uint32, 1),
        ('entropy_coding_mode_flag', ctypes.c_uint32, 1),
        ('pic_scaling_matrix_present_flag', ctypes.c_uint32, 1),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH264PictureParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'transform_8x8_mode_flag': {'python_name': ['transform', '8x8', 'mode', 'flag']},
        'redundant_pic_cnt_present_flag': {'python_name': ['redundant', 'pic', 'cnt', 'present', 'flag']},
        'constrained_intra_pred_flag': {'python_name': ['constrained', 'intra', 'pred', 'flag']},
        'deblocking_filter_control_present_flag': {'python_name': ['deblocking', 'filter', 'control', 'present', 'flag']},
        'weighted_pred_flag': {'python_name': ['weighted', 'pred', 'flag']},
        'bottom_field_pic_order_in_frame_present_flag': {'python_name': ['bottom', 'field', 'pic', 'order', 'in', 'frame', 'present', 'flag']},
        'entropy_coding_mode_flag': {'python_name': ['entropy', 'coding', 'mode', 'flag']},
        'pic_scaling_matrix_present_flag': {'python_name': ['pic', 'scaling', 'matrix', 'present', 'flag']},
    }
}
