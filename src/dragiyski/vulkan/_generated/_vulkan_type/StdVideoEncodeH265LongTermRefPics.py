import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('num_long_term_sps', ctypes.c_uint8),
        ('num_long_term_pics', ctypes.c_uint8),
        ('lt_idx_sps', ctypes.ARRAY(ctypes.c_uint8, 32)),
        ('poc_lsb_lt', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('used_by_curr_pic_lt_flag', ctypes.c_uint16),
        ('delta_poc_msb_present_flag', ctypes.ARRAY(ctypes.c_uint8, 48)),
        ('delta_poc_msb_cycle_lt', ctypes.ARRAY(ctypes.c_uint8, 48)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH265PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'num_long_term_sps': {'python_name': ['num', 'long', 'term', 'sps']},
        'num_long_term_pics': {'python_name': ['num', 'long', 'term', 'pics']},
        'lt_idx_sps': {'python_name': ['lt', 'idx', 'sps']},
        'poc_lsb_lt': {'python_name': ['poc', 'lsb', 'lt']},
        'used_by_curr_pic_lt_flag': {'python_name': ['used', 'by', 'curr', 'pic', 'lt', 'flag']},
        'delta_poc_msb_present_flag': {'python_name': ['delta', 'poc', 'msb', 'present', 'flag']},
        'delta_poc_msb_cycle_lt': {'python_name': ['delta', 'poc', 'msb', 'cycle', 'lt']},
    }
}
