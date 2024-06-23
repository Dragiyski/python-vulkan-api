import ctypes

class CType(ctypes.Structure):
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH264SequenceParameterSetVui',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'cpb_cnt_minus1': {'python_name': ['cpb', 'cnt', 'minus1']},
        'bit_rate_scale': {'python_name': ['bit', 'rate', 'scale']},
        'cpb_size_scale': {'python_name': ['cpb', 'size', 'scale']},
        'reserved1': {'python_name': ['reserved1']},
        'bit_rate_value_minus1': {'python_name': ['bit', 'rate', 'value', 'minus1']},
        'cpb_size_value_minus1': {'python_name': ['cpb', 'size', 'value', 'minus1']},
        'cbr_flag': {'python_name': ['cbr', 'flag']},
        'initial_cpb_removal_delay_length_minus1': {'python_name': ['initial', 'cpb', 'removal', 'delay', 'length', 'minus1']},
        'cpb_removal_delay_length_minus1': {'python_name': ['cpb', 'removal', 'delay', 'length', 'minus1']},
        'dpb_output_delay_length_minus1': {'python_name': ['dpb', 'output', 'delay', 'length', 'minus1']},
        'time_offset_length': {'python_name': ['time', 'offset', 'length']},
    }
}
