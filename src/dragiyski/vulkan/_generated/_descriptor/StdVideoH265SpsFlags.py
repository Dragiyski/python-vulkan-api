from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265SpsFlags'
_member_list_ = ['sps_temporal_id_nesting_flag', 'separate_colour_plane_flag', 'conformance_window_flag', 'sps_sub_layer_ordering_info_present_flag', 'scaling_list_enabled_flag', 'sps_scaling_list_data_present_flag', 'amp_enabled_flag', 'sample_adaptive_offset_enabled_flag', 'pcm_enabled_flag', 'pcm_loop_filter_disabled_flag', 'long_term_ref_pics_present_flag', 'sps_temporal_mvp_enabled_flag', 'strong_intra_smoothing_enabled_flag', 'vui_parameters_present_flag', 'sps_extension_present_flag', 'sps_range_extension_flag', 'transform_skip_rotation_enabled_flag', 'transform_skip_context_enabled_flag', 'implicit_rdpcm_enabled_flag', 'explicit_rdpcm_enabled_flag', 'extended_precision_processing_flag', 'intra_smoothing_disabled_flag', 'high_precision_offsets_enabled_flag', 'persistent_rice_adaptation_enabled_flag', 'cabac_bypass_alignment_enabled_flag', 'sps_scc_extension_flag', 'sps_curr_pic_ref_enabled_flag', 'palette_mode_enabled_flag', 'sps_palette_predictor_initializers_present_flag', 'intra_boundary_filtering_disabled_flag']
_member_info_ = {
    'sps_temporal_id_nesting_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'separate_colour_plane_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'conformance_window_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_sub_layer_ordering_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'scaling_list_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_scaling_list_data_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'amp_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sample_adaptive_offset_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pcm_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pcm_loop_filter_disabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'long_term_ref_pics_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_temporal_mvp_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'strong_intra_smoothing_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vui_parameters_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_extension_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_range_extension_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'transform_skip_rotation_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'transform_skip_context_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'implicit_rdpcm_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'explicit_rdpcm_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'extended_precision_processing_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'intra_smoothing_disabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'high_precision_offsets_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'persistent_rice_adaptation_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'cabac_bypass_alignment_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_scc_extension_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_curr_pic_ref_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'palette_mode_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sps_palette_predictor_initializers_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'intra_boundary_filtering_disabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
