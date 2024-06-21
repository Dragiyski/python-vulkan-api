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
