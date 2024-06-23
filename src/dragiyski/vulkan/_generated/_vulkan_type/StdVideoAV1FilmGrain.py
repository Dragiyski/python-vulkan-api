import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1FilmGrainFlags import CType as StdVideoAV1FilmGrainFlags

CType._fields_ = [
    ('flags', StdVideoAV1FilmGrainFlags),
    ('grain_scaling_minus_8', ctypes.c_uint8),
    ('ar_coeff_lag', ctypes.c_uint8),
    ('ar_coeff_shift_minus_6', ctypes.c_uint8),
    ('grain_scale_shift', ctypes.c_uint8),
    ('grain_seed', ctypes.c_uint16),
    ('film_grain_params_ref_idx', ctypes.c_uint8),
    ('num_y_points', ctypes.c_uint8),
    ('point_y_value', ctypes.ARRAY(ctypes.c_uint8, 14)),
    ('point_y_scaling', ctypes.ARRAY(ctypes.c_uint8, 14)),
    ('num_cb_points', ctypes.c_uint8),
    ('point_cb_value', ctypes.ARRAY(ctypes.c_uint8, 10)),
    ('point_cb_scaling', ctypes.ARRAY(ctypes.c_uint8, 10)),
    ('num_cr_points', ctypes.c_uint8),
    ('point_cr_value', ctypes.ARRAY(ctypes.c_uint8, 10)),
    ('point_cr_scaling', ctypes.ARRAY(ctypes.c_uint8, 10)),
    ('ar_coeffs_y_plus_128', ctypes.ARRAY(ctypes.c_int8, 24)),
    ('ar_coeffs_cb_plus_128', ctypes.ARRAY(ctypes.c_int8, 25)),
    ('ar_coeffs_cr_plus_128', ctypes.ARRAY(ctypes.c_int8, 25)),
    ('cb_mult', ctypes.c_uint8),
    ('cb_luma_mult', ctypes.c_uint8),
    ('cb_offset', ctypes.c_uint16),
    ('cr_mult', ctypes.c_uint8),
    ('cr_luma_mult', ctypes.c_uint8),
    ('cr_offset', ctypes.c_uint16),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1FilmGrainFlags',
    },
    'included_in': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoAV1FilmGrainFlags'},
        'grain_scaling_minus_8': {'python_name': ['grain', 'scaling', 'minus', '8']},
        'ar_coeff_lag': {'python_name': ['ar', 'coeff', 'lag']},
        'ar_coeff_shift_minus_6': {'python_name': ['ar', 'coeff', 'shift', 'minus', '6']},
        'grain_scale_shift': {'python_name': ['grain', 'scale', 'shift']},
        'grain_seed': {'python_name': ['grain', 'seed']},
        'film_grain_params_ref_idx': {'python_name': ['film', 'grain', 'params', 'ref', 'idx']},
        'num_y_points': {'python_name': ['num', 'y', 'points']},
        'point_y_value': {'python_name': ['point', 'y', 'value']},
        'point_y_scaling': {'python_name': ['point', 'y', 'scaling']},
        'num_cb_points': {'python_name': ['num', 'cb', 'points']},
        'point_cb_value': {'python_name': ['point', 'cb', 'value']},
        'point_cb_scaling': {'python_name': ['point', 'cb', 'scaling']},
        'num_cr_points': {'python_name': ['num', 'cr', 'points']},
        'point_cr_value': {'python_name': ['point', 'cr', 'value']},
        'point_cr_scaling': {'python_name': ['point', 'cr', 'scaling']},
        'ar_coeffs_y_plus_128': {'python_name': ['ar', 'coeffs', 'y', 'plus', '128']},
        'ar_coeffs_cb_plus_128': {'python_name': ['ar', 'coeffs', 'cb', 'plus', '128']},
        'ar_coeffs_cr_plus_128': {'python_name': ['ar', 'coeffs', 'cr', 'plus', '128']},
        'cb_mult': {'python_name': ['cb', 'mult']},
        'cb_luma_mult': {'python_name': ['cb', 'luma', 'mult']},
        'cb_offset': {'python_name': ['cb', 'offset']},
        'cr_mult': {'python_name': ['cr', 'mult']},
        'cr_luma_mult': {'python_name': ['cr', 'luma', 'mult']},
        'cr_offset': {'python_name': ['cr', 'offset']},
    }
}
