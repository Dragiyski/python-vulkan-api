import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('memory_management_control_operation', ctypes.c_int),
        ('difference_of_pic_nums_minus1', ctypes.c_uint16),
        ('long_term_pic_num', ctypes.c_uint16),
        ('long_term_frame_idx', ctypes.c_uint16),
        ('max_long_term_frame_idx_plus1', ctypes.c_uint16),
    ]
