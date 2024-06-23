import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('IdrPicFlag', ctypes.c_uint32, 1),
        ('is_reference', ctypes.c_uint32, 1),
        ('no_output_of_prior_pics_flag', ctypes.c_uint32, 1),
        ('long_term_reference_flag', ctypes.c_uint32, 1),
        ('adaptive_ref_pic_marking_mode_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 27),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH264PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'IdrPicFlag': {'python_name': ['idr', 'pic', 'flag']},
        'is_reference': {'python_name': ['is', 'reference']},
        'no_output_of_prior_pics_flag': {'python_name': ['no', 'output', 'of', 'prior', 'pics', 'flag']},
        'long_term_reference_flag': {'python_name': ['long', 'term', 'reference', 'flag']},
        'adaptive_ref_pic_marking_mode_flag': {'python_name': ['adaptive', 'ref', 'pic', 'marking', 'mode', 'flag']},
        'reserved': {'python_name': ['reserved']},
    }
}
