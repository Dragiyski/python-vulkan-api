import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('luma_weight_l0_flag', ctypes.c_uint16),
        ('chroma_weight_l0_flag', ctypes.c_uint16),
        ('luma_weight_l1_flag', ctypes.c_uint16),
        ('chroma_weight_l1_flag', ctypes.c_uint16),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH265WeightTable',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'luma_weight_l0_flag': {'python_name': ['luma', 'weight', 'l0', 'flag']},
        'chroma_weight_l0_flag': {'python_name': ['chroma', 'weight', 'l0', 'flag']},
        'luma_weight_l1_flag': {'python_name': ['luma', 'weight', 'l1', 'flag']},
        'chroma_weight_l1_flag': {'python_name': ['chroma', 'weight', 'l1', 'flag']},
    }
}
