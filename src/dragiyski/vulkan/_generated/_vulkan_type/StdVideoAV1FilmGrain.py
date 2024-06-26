import ctypes

class StdVideoAV1FilmGrain(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'flags': 'flags',
        'grain_scaling_minus_8': 'grain_scaling_minus_8',
        'ar_coeff_lag': 'ar_coeff_lag',
        'ar_coeff_shift_minus_6': 'ar_coeff_shift_minus_6',
        'grain_scale_shift': 'grain_scale_shift',
        'grain_seed': 'grain_seed',
        'film_grain_params_ref_idx': 'film_grain_params_ref_idx',
        'num_y_points': 'num_y_points',
        'point_y_value': 'point_y_value',
        'point_y_scaling': 'point_y_scaling',
        'num_cb_points': 'num_cb_points',
        'point_cb_value': 'point_cb_value',
        'point_cb_scaling': 'point_cb_scaling',
        'num_cr_points': 'num_cr_points',
        'point_cr_value': 'point_cr_value',
        'point_cr_scaling': 'point_cr_scaling',
        'ar_coeffs_y_plus_128': 'ar_coeffs_y_plus_128',
        'ar_coeffs_cb_plus_128': 'ar_coeffs_cb_plus_128',
        'ar_coeffs_cr_plus_128': 'ar_coeffs_cr_plus_128',
        'cb_mult': 'cb_mult',
        'cb_luma_mult': 'cb_luma_mult',
        'cb_offset': 'cb_offset',
        'cr_mult': 'cr_mult',
        'cr_luma_mult': 'cr_luma_mult',
        'cr_offset': 'cr_offset',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoAV1FilmGrainFlags import StdVideoAV1FilmGrainFlags

StdVideoAV1FilmGrain._fields_ = [
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

StdVideoAV1FilmGrain._type_ = {
    'flags': StdVideoAV1FilmGrainFlags,
    'grain_scaling_minus_8': ctypes.c_uint8,
    'ar_coeff_lag': ctypes.c_uint8,
    'ar_coeff_shift_minus_6': ctypes.c_uint8,
    'grain_scale_shift': ctypes.c_uint8,
    'grain_seed': ctypes.c_uint16,
    'film_grain_params_ref_idx': ctypes.c_uint8,
    'num_y_points': ctypes.c_uint8,
    'point_y_value': ctypes.ARRAY(ctypes.c_uint8, 14),
    'point_y_scaling': ctypes.ARRAY(ctypes.c_uint8, 14),
    'num_cb_points': ctypes.c_uint8,
    'point_cb_value': ctypes.ARRAY(ctypes.c_uint8, 10),
    'point_cb_scaling': ctypes.ARRAY(ctypes.c_uint8, 10),
    'num_cr_points': ctypes.c_uint8,
    'point_cr_value': ctypes.ARRAY(ctypes.c_uint8, 10),
    'point_cr_scaling': ctypes.ARRAY(ctypes.c_uint8, 10),
    'ar_coeffs_y_plus_128': ctypes.ARRAY(ctypes.c_int8, 24),
    'ar_coeffs_cb_plus_128': ctypes.ARRAY(ctypes.c_int8, 25),
    'ar_coeffs_cr_plus_128': ctypes.ARRAY(ctypes.c_int8, 25),
    'cb_mult': ctypes.c_uint8,
    'cb_luma_mult': ctypes.c_uint8,
    'cb_offset': ctypes.c_uint16,
    'cr_mult': ctypes.c_uint8,
    'cr_luma_mult': ctypes.c_uint8,
    'cr_offset': ctypes.c_uint16,
}
