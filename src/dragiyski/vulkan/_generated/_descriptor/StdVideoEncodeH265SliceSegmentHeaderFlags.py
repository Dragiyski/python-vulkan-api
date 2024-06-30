from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265SliceSegmentHeaderFlags'
_member_list_ = ['first_slice_segment_in_pic_flag', 'dependent_slice_segment_flag', 'slice_sao_luma_flag', 'slice_sao_chroma_flag', 'num_ref_idx_active_override_flag', 'mvd_l1_zero_flag', 'cabac_init_flag', 'cu_chroma_qp_offset_enabled_flag', 'deblocking_filter_override_flag', 'slice_deblocking_filter_disabled_flag', 'collocated_from_l0_flag', 'slice_loop_filter_across_slices_enabled_flag', 'reserved']
_member_info_ = {
    'first_slice_segment_in_pic_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'dependent_slice_segment_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'slice_sao_luma_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'slice_sao_chroma_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'num_ref_idx_active_override_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'mvd_l1_zero_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'cabac_init_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'cu_chroma_qp_offset_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'deblocking_filter_override_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'slice_deblocking_filter_disabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'collocated_from_l0_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'slice_loop_filter_across_slices_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 20,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoEncodeH265SliceSegmentHeader',
}
_input_of_ = set()
_output_of_ = set()
