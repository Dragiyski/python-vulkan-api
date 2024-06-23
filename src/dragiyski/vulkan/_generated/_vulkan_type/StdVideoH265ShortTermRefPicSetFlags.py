import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('inter_ref_pic_set_prediction_flag', ctypes.c_uint32, 1),
        ('delta_rps_sign', ctypes.c_uint32, 1),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoH265ShortTermRefPicSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'inter_ref_pic_set_prediction_flag': {'python_name': ['inter', 'ref', 'pic', 'set', 'prediction', 'flag']},
        'delta_rps_sign': {'python_name': ['delta', 'rps', 'sign']},
    }
}
