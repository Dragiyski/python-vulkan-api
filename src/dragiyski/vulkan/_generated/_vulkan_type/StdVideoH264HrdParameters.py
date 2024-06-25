import ctypes

class StdVideoH264HrdParameters(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'cpb_cnt_minus1': ctypes.c_uint8,
            'bit_rate_scale': ctypes.c_uint8,
            'cpb_size_scale': ctypes.c_uint8,
            'reserved1': ctypes.c_uint8,
            'bit_rate_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
            'cpb_size_value_minus1': ctypes.ARRAY(ctypes.c_uint32, 32),
            'cbr_flag': ctypes.ARRAY(ctypes.c_uint8, 32),
            'initial_cpb_removal_delay_length_minus1': ctypes.c_uint32,
            'cpb_removal_delay_length_minus1': ctypes.c_uint32,
            'dpb_output_delay_length_minus1': ctypes.c_uint32,
            'time_offset_length': ctypes.c_uint32,
        }

    _fields_ = [
        ('cpb_cnt_minus1', ctypes.c_uint8),
        ('bit_rate_scale', ctypes.c_uint8),
        ('cpb_size_scale', ctypes.c_uint8),
        ('reserved1', ctypes.c_uint8),
        ('bit_rate_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cbr_flag', ctypes.ARRAY(ctypes.c_uint8, 32)),
        ('initial_cpb_removal_delay_length_minus1', ctypes.c_uint32),
        ('cpb_removal_delay_length_minus1', ctypes.c_uint32),
        ('dpb_output_delay_length_minus1', ctypes.c_uint32),
        ('time_offset_length', ctypes.c_uint32),
    ]
