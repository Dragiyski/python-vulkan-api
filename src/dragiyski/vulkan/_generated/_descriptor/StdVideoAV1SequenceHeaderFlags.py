from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1SequenceHeaderFlags'
_member_list_ = ['still_picture', 'reduced_still_picture_header', 'use_128x128_superblock', 'enable_filter_intra', 'enable_intra_edge_filter', 'enable_interintra_compound', 'enable_masked_compound', 'enable_warped_motion', 'enable_dual_filter', 'enable_order_hint', 'enable_jnt_comp', 'enable_ref_frame_mvs', 'frame_id_numbers_present_flag', 'enable_superres', 'enable_cdef', 'enable_restoration', 'film_grain_params_present', 'timing_info_present_flag', 'initial_display_delay_present_flag', 'reserved']
_member_info_ = {
    'still_picture': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reduced_still_picture_header': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'use_128x128_superblock': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_filter_intra': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_intra_edge_filter': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_interintra_compound': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_masked_compound': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_warped_motion': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_dual_filter': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_order_hint': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_jnt_comp': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_ref_frame_mvs': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'frame_id_numbers_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_superres': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_cdef': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'enable_restoration': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'film_grain_params_present': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'timing_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'initial_display_delay_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 13,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoAV1SequenceHeader',
}
_input_of_ = set()
_output_of_ = set()
