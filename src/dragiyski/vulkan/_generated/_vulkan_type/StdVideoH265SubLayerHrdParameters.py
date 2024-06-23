import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('bit_rate_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cpb_size_du_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('bit_rate_du_value_minus1', ctypes.ARRAY(ctypes.c_uint32, 32)),
        ('cbr_flag', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265HrdParameters',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'bit_rate_value_minus1': {'python_name': ['bit', 'rate', 'value', 'minus1']},
        'cpb_size_value_minus1': {'python_name': ['cpb', 'size', 'value', 'minus1']},
        'cpb_size_du_value_minus1': {'python_name': ['cpb', 'size', 'du', 'value', 'minus1']},
        'bit_rate_du_value_minus1': {'python_name': ['bit', 'rate', 'du', 'value', 'minus1']},
        'cbr_flag': {'python_name': ['cbr', 'flag']},
    }
}
