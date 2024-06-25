import ctypes

class StdVideoEncodeH264RefPicMarkingEntry(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'memory_management_control_operation': ctypes.c_int,
            'difference_of_pic_nums_minus1': ctypes.c_uint16,
            'long_term_pic_num': ctypes.c_uint16,
            'long_term_frame_idx': ctypes.c_uint16,
            'max_long_term_frame_idx_plus1': ctypes.c_uint16,
        }

    _fields_ = [
        ('memory_management_control_operation', ctypes.c_int),
        ('difference_of_pic_nums_minus1', ctypes.c_uint16),
        ('long_term_pic_num', ctypes.c_uint16),
        ('long_term_frame_idx', ctypes.c_uint16),
        ('max_long_term_frame_idx_plus1', ctypes.c_uint16),
    ]
