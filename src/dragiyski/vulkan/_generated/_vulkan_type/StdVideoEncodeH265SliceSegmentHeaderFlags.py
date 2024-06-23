import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('first_slice_segment_in_pic_flag', ctypes.c_uint32, 1),
        ('dependent_slice_segment_flag', ctypes.c_uint32, 1),
        ('slice_sao_luma_flag', ctypes.c_uint32, 1),
        ('slice_sao_chroma_flag', ctypes.c_uint32, 1),
        ('num_ref_idx_active_override_flag', ctypes.c_uint32, 1),
        ('mvd_l1_zero_flag', ctypes.c_uint32, 1),
        ('cabac_init_flag', ctypes.c_uint32, 1),
        ('cu_chroma_qp_offset_enabled_flag', ctypes.c_uint32, 1),
        ('deblocking_filter_override_flag', ctypes.c_uint32, 1),
        ('slice_deblocking_filter_disabled_flag', ctypes.c_uint32, 1),
        ('collocated_from_l0_flag', ctypes.c_uint32, 1),
        ('slice_loop_filter_across_slices_enabled_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 20),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH265SliceSegmentHeader',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'first_slice_segment_in_pic_flag': {'python_name': ['first', 'slice', 'segment', 'in', 'pic', 'flag']},
        'dependent_slice_segment_flag': {'python_name': ['dependent', 'slice', 'segment', 'flag']},
        'slice_sao_luma_flag': {'python_name': ['slice', 'sao', 'luma', 'flag']},
        'slice_sao_chroma_flag': {'python_name': ['slice', 'sao', 'chroma', 'flag']},
        'num_ref_idx_active_override_flag': {'python_name': ['num', 'ref', 'idx', 'active', 'override', 'flag']},
        'mvd_l1_zero_flag': {'python_name': ['mvd', 'l1', 'zero', 'flag']},
        'cabac_init_flag': {'python_name': ['cabac', 'init', 'flag']},
        'cu_chroma_qp_offset_enabled_flag': {'python_name': ['cu', 'chroma', 'qp', 'offset', 'enabled', 'flag']},
        'deblocking_filter_override_flag': {'python_name': ['deblocking', 'filter', 'override', 'flag']},
        'slice_deblocking_filter_disabled_flag': {'python_name': ['slice', 'deblocking', 'filter', 'disabled', 'flag']},
        'collocated_from_l0_flag': {'python_name': ['collocated', 'from', 'l0', 'flag']},
        'slice_loop_filter_across_slices_enabled_flag': {'python_name': ['slice', 'loop', 'filter', 'across', 'slices', 'enabled', 'flag']},
        'reserved': {'python_name': ['reserved']},
    }
}
