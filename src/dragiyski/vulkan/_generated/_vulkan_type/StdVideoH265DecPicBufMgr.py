import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('max_latency_increase_plus1', ctypes.ARRAY(ctypes.c_uint32, 7)),
        ('max_dec_pic_buffering_minus1', ctypes.ARRAY(ctypes.c_uint8, 7)),
        ('max_num_reorder_pics', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265SequenceParameterSet',
        'StdVideoH265VideoParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'max_latency_increase_plus1': {'python_name': ['max', 'latency', 'increase', 'plus1']},
        'max_dec_pic_buffering_minus1': {'python_name': ['max', 'dec', 'pic', 'buffering', 'minus1']},
        'max_num_reorder_pics': {'python_name': ['max', 'num', 'reorder', 'pics']},
    }
}
