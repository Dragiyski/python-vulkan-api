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
