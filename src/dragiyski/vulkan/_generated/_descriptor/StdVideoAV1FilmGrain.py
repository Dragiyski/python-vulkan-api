from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1FilmGrain'
_member_list_ = ['flags', 'grain_scaling_minus_8', 'ar_coeff_lag', 'ar_coeff_shift_minus_6', 'grain_scale_shift', 'grain_seed', 'film_grain_params_ref_idx', 'num_y_points', 'point_y_value', 'point_y_scaling', 'num_cb_points', 'point_cb_value', 'point_cb_scaling', 'num_cr_points', 'point_cr_value', 'point_cr_scaling', 'ar_coeffs_y_plus_128', 'ar_coeffs_cb_plus_128', 'ar_coeffs_cr_plus_128', 'cb_mult', 'cb_luma_mult', 'cb_offset', 'cr_mult', 'cr_luma_mult', 'cr_offset']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoAV1FilmGrainFlags'),
        'type_name': 'StdVideoAV1FilmGrainFlags',
        'structure': 'StdVideoAV1FilmGrainFlags',
        'is_string': False,
    },
    'grain_scaling_minus_8': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'ar_coeff_lag': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'ar_coeff_shift_minus_6': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'grain_scale_shift': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'grain_seed': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'film_grain_params_ref_idx': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_y_points': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'point_y_value': {
        'type': CArrayType(CIntType('c_uint8'), 14),
        'is_string': False,
    },
    'point_y_scaling': {
        'type': CArrayType(CIntType('c_uint8'), 14),
        'is_string': False,
    },
    'num_cb_points': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'point_cb_value': {
        'type': CArrayType(CIntType('c_uint8'), 10),
        'is_string': False,
    },
    'point_cb_scaling': {
        'type': CArrayType(CIntType('c_uint8'), 10),
        'is_string': False,
    },
    'num_cr_points': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'point_cr_value': {
        'type': CArrayType(CIntType('c_uint8'), 10),
        'is_string': False,
    },
    'point_cr_scaling': {
        'type': CArrayType(CIntType('c_uint8'), 10),
        'is_string': False,
    },
    'ar_coeffs_y_plus_128': {
        'type': CArrayType(CIntType('c_int8'), 24),
        'is_string': False,
    },
    'ar_coeffs_cb_plus_128': {
        'type': CArrayType(CIntType('c_int8'), 25),
        'is_string': False,
    },
    'ar_coeffs_cr_plus_128': {
        'type': CArrayType(CIntType('c_int8'), 25),
        'is_string': False,
    },
    'cb_mult': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cb_luma_mult': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cb_offset': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'cr_mult': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cr_luma_mult': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cr_offset': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1FilmGrainFlags',
}
_included_in_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
