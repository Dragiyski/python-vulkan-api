from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265PpsFlags'
_member_list_ = ['dependent_slice_segments_enabled_flag', 'output_flag_present_flag', 'sign_data_hiding_enabled_flag', 'cabac_init_present_flag', 'constrained_intra_pred_flag', 'transform_skip_enabled_flag', 'cu_qp_delta_enabled_flag', 'pps_slice_chroma_qp_offsets_present_flag', 'weighted_pred_flag', 'weighted_bipred_flag', 'transquant_bypass_enabled_flag', 'tiles_enabled_flag', 'entropy_coding_sync_enabled_flag', 'uniform_spacing_flag', 'loop_filter_across_tiles_enabled_flag', 'pps_loop_filter_across_slices_enabled_flag', 'deblocking_filter_control_present_flag', 'deblocking_filter_override_enabled_flag', 'pps_deblocking_filter_disabled_flag', 'pps_scaling_list_data_present_flag', 'lists_modification_present_flag', 'slice_segment_header_extension_present_flag', 'pps_extension_present_flag', 'cross_component_prediction_enabled_flag', 'chroma_qp_offset_list_enabled_flag', 'pps_curr_pic_ref_enabled_flag', 'residual_adaptive_colour_transform_enabled_flag', 'pps_slice_act_qp_offsets_present_flag', 'pps_palette_predictor_initializers_present_flag', 'monochrome_palette_flag', 'pps_range_extension_flag']
_member_info_ = {
    'dependent_slice_segments_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'output_flag_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sign_data_hiding_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'cabac_init_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'constrained_intra_pred_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'transform_skip_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'cu_qp_delta_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_slice_chroma_qp_offsets_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'weighted_pred_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'weighted_bipred_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'transquant_bypass_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'tiles_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'entropy_coding_sync_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'uniform_spacing_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'loop_filter_across_tiles_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_loop_filter_across_slices_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'deblocking_filter_control_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'deblocking_filter_override_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_deblocking_filter_disabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_scaling_list_data_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'lists_modification_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'slice_segment_header_extension_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_extension_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'cross_component_prediction_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'chroma_qp_offset_list_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_curr_pic_ref_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'residual_adaptive_colour_transform_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_slice_act_qp_offsets_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_palette_predictor_initializers_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'monochrome_palette_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pps_range_extension_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265PictureParameterSet',
}
_input_of_ = set()
_output_of_ = set()
