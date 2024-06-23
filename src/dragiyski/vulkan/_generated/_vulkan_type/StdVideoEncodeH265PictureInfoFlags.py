import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('is_reference', ctypes.c_uint32, 1),
        ('IrapPicFlag', ctypes.c_uint32, 1),
        ('used_for_long_term_reference', ctypes.c_uint32, 1),
        ('discardable_flag', ctypes.c_uint32, 1),
        ('cross_layer_bla_flag', ctypes.c_uint32, 1),
        ('pic_output_flag', ctypes.c_uint32, 1),
        ('no_output_of_prior_pics_flag', ctypes.c_uint32, 1),
        ('short_term_ref_pic_set_sps_flag', ctypes.c_uint32, 1),
        ('slice_temporal_mvp_enabled_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 23),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH265PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'is_reference': {'python_name': ['is', 'reference']},
        'IrapPicFlag': {'python_name': ['irap', 'pic', 'flag']},
        'used_for_long_term_reference': {'python_name': ['used', 'for', 'long', 'term', 'reference']},
        'discardable_flag': {'python_name': ['discardable', 'flag']},
        'cross_layer_bla_flag': {'python_name': ['cross', 'layer', 'bla', 'flag']},
        'pic_output_flag': {'python_name': ['pic', 'output', 'flag']},
        'no_output_of_prior_pics_flag': {'python_name': ['no', 'output', 'of', 'prior', 'pics', 'flag']},
        'short_term_ref_pic_set_sps_flag': {'python_name': ['short', 'term', 'ref', 'pic', 'set', 'sps', 'flag']},
        'slice_temporal_mvp_enabled_flag': {'python_name': ['slice', 'temporal', 'mvp', 'enabled', 'flag']},
        'reserved': {'python_name': ['reserved']},
    }
}
