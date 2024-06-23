import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('direct_spatial_mv_pred_flag', ctypes.c_uint32, 1),
        ('num_ref_idx_active_override_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoEncodeH264SliceHeader',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'direct_spatial_mv_pred_flag': {'python_name': ['direct', 'spatial', 'mv', 'pred', 'flag']},
        'num_ref_idx_active_override_flag': {'python_name': ['num', 'ref', 'idx', 'active', 'override', 'flag']},
        'reserved': {'python_name': ['reserved']},
    }
}
