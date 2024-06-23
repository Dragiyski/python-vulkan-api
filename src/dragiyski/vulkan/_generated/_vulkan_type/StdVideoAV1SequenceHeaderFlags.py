import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('still_picture', ctypes.c_uint32, 1),
        ('reduced_still_picture_header', ctypes.c_uint32, 1),
        ('use_128x128_superblock', ctypes.c_uint32, 1),
        ('enable_filter_intra', ctypes.c_uint32, 1),
        ('enable_intra_edge_filter', ctypes.c_uint32, 1),
        ('enable_interintra_compound', ctypes.c_uint32, 1),
        ('enable_masked_compound', ctypes.c_uint32, 1),
        ('enable_warped_motion', ctypes.c_uint32, 1),
        ('enable_dual_filter', ctypes.c_uint32, 1),
        ('enable_order_hint', ctypes.c_uint32, 1),
        ('enable_jnt_comp', ctypes.c_uint32, 1),
        ('enable_ref_frame_mvs', ctypes.c_uint32, 1),
        ('frame_id_numbers_present_flag', ctypes.c_uint32, 1),
        ('enable_superres', ctypes.c_uint32, 1),
        ('enable_cdef', ctypes.c_uint32, 1),
        ('enable_restoration', ctypes.c_uint32, 1),
        ('film_grain_params_present', ctypes.c_uint32, 1),
        ('timing_info_present_flag', ctypes.c_uint32, 1),
        ('initial_display_delay_present_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 13),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoAV1SequenceHeader',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'still_picture': {'python_name': ['still', 'picture']},
        'reduced_still_picture_header': {'python_name': ['reduced', 'still', 'picture', 'header']},
        'use_128x128_superblock': {'python_name': ['use', '128x128', 'superblock']},
        'enable_filter_intra': {'python_name': ['enable', 'filter', 'intra']},
        'enable_intra_edge_filter': {'python_name': ['enable', 'intra', 'edge', 'filter']},
        'enable_interintra_compound': {'python_name': ['enable', 'interintra', 'compound']},
        'enable_masked_compound': {'python_name': ['enable', 'masked', 'compound']},
        'enable_warped_motion': {'python_name': ['enable', 'warped', 'motion']},
        'enable_dual_filter': {'python_name': ['enable', 'dual', 'filter']},
        'enable_order_hint': {'python_name': ['enable', 'order', 'hint']},
        'enable_jnt_comp': {'python_name': ['enable', 'jnt', 'comp']},
        'enable_ref_frame_mvs': {'python_name': ['enable', 'ref', 'frame', 'mvs']},
        'frame_id_numbers_present_flag': {'python_name': ['frame', 'id', 'numbers', 'present', 'flag']},
        'enable_superres': {'python_name': ['enable', 'superres']},
        'enable_cdef': {'python_name': ['enable', 'cdef']},
        'enable_restoration': {'python_name': ['enable', 'restoration']},
        'film_grain_params_present': {'python_name': ['film', 'grain', 'params', 'present']},
        'timing_info_present_flag': {'python_name': ['timing', 'info', 'present', 'flag']},
        'initial_display_delay_present_flag': {'python_name': ['initial', 'display', 'delay', 'present', 'flag']},
        'reserved': {'python_name': ['reserved']},
    }
}
