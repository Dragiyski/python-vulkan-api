import ctypes

class StdVideoH265ShortTermRefPicSet(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoH265ShortTermRefPicSetFlags,
            'delta_idx_minus1': ctypes.c_uint32,
            'use_delta_flag': ctypes.c_uint16,
            'abs_delta_rps_minus1': ctypes.c_uint16,
            'used_by_curr_pic_flag': ctypes.c_uint16,
            'used_by_curr_pic_s0_flag': ctypes.c_uint16,
            'used_by_curr_pic_s1_flag': ctypes.c_uint16,
            'reserved1': ctypes.c_uint16,
            'reserved2': ctypes.c_uint8,
            'reserved3': ctypes.c_uint8,
            'num_negative_pics': ctypes.c_uint8,
            'num_positive_pics': ctypes.c_uint8,
            'delta_poc_s0_minus1': ctypes.ARRAY(ctypes.c_uint16, 16),
            'delta_poc_s1_minus1': ctypes.ARRAY(ctypes.c_uint16, 16),
        }


from .StdVideoH265ShortTermRefPicSetFlags import StdVideoH265ShortTermRefPicSetFlags

StdVideoH265ShortTermRefPicSet._fields_ = [
    ('flags', StdVideoH265ShortTermRefPicSetFlags),
    ('delta_idx_minus1', ctypes.c_uint32),
    ('use_delta_flag', ctypes.c_uint16),
    ('abs_delta_rps_minus1', ctypes.c_uint16),
    ('used_by_curr_pic_flag', ctypes.c_uint16),
    ('used_by_curr_pic_s0_flag', ctypes.c_uint16),
    ('used_by_curr_pic_s1_flag', ctypes.c_uint16),
    ('reserved1', ctypes.c_uint16),
    ('reserved2', ctypes.c_uint8),
    ('reserved3', ctypes.c_uint8),
    ('num_negative_pics', ctypes.c_uint8),
    ('num_positive_pics', ctypes.c_uint8),
    ('delta_poc_s0_minus1', ctypes.ARRAY(ctypes.c_uint16, 16)),
    ('delta_poc_s1_minus1', ctypes.ARRAY(ctypes.c_uint16, 16)),
]
