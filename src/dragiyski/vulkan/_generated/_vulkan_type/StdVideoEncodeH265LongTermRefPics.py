import ctypes

class StdVideoEncodeH265LongTermRefPics(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'num_long_term_sps': ctypes.c_uint8,
            'num_long_term_pics': ctypes.c_uint8,
            'lt_idx_sps': ctypes.ARRAY(ctypes.c_uint8, 32),
            'poc_lsb_lt': ctypes.ARRAY(ctypes.c_uint8, 16),
            'used_by_curr_pic_lt_flag': ctypes.c_uint16,
            'delta_poc_msb_present_flag': ctypes.ARRAY(ctypes.c_uint8, 48),
            'delta_poc_msb_cycle_lt': ctypes.ARRAY(ctypes.c_uint8, 48),
        }

    _fields_ = [
        ('num_long_term_sps', ctypes.c_uint8),
        ('num_long_term_pics', ctypes.c_uint8),
        ('lt_idx_sps', ctypes.ARRAY(ctypes.c_uint8, 32)),
        ('poc_lsb_lt', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('used_by_curr_pic_lt_flag', ctypes.c_uint16),
        ('delta_poc_msb_present_flag', ctypes.ARRAY(ctypes.c_uint8, 48)),
        ('delta_poc_msb_cycle_lt', ctypes.ARRAY(ctypes.c_uint8, 48)),
    ]
