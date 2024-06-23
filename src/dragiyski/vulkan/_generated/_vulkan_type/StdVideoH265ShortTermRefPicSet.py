import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265ShortTermRefPicSetFlags import CType as StdVideoH265ShortTermRefPicSetFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH265ShortTermRefPicSetFlags',
    },
    'included_in': {
        'StdVideoEncodeH265PictureInfo',
        'StdVideoH265SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH265ShortTermRefPicSetFlags'},
        'delta_idx_minus1': {'python_name': ['delta', 'idx', 'minus1']},
        'use_delta_flag': {'python_name': ['use', 'delta', 'flag']},
        'abs_delta_rps_minus1': {'python_name': ['abs', 'delta', 'rps', 'minus1']},
        'used_by_curr_pic_flag': {'python_name': ['used', 'by', 'curr', 'pic', 'flag']},
        'used_by_curr_pic_s0_flag': {'python_name': ['used', 'by', 'curr', 'pic', 's0', 'flag']},
        'used_by_curr_pic_s1_flag': {'python_name': ['used', 'by', 'curr', 'pic', 's1', 'flag']},
        'reserved1': {'python_name': ['reserved1']},
        'reserved2': {'python_name': ['reserved2']},
        'reserved3': {'python_name': ['reserved3']},
        'num_negative_pics': {'python_name': ['num', 'negative', 'pics']},
        'num_positive_pics': {'python_name': ['num', 'positive', 'pics']},
        'delta_poc_s0_minus1': {'python_name': ['delta', 'poc', 's0', 'minus1']},
        'delta_poc_s1_minus1': {'python_name': ['delta', 'poc', 's1', 'minus1']},
    }
}
