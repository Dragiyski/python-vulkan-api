from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeAV1PictureInfoFlags'
_member_list_ = ['error_resilient_mode', 'disable_cdf_update', 'use_superres', 'render_and_frame_size_different', 'allow_screen_content_tools', 'is_filter_switchable', 'force_integer_mv', 'frame_size_override_flag', 'buffer_removal_time_present_flag', 'allow_intrabc', 'frame_refs_short_signaling', 'allow_high_precision_mv', 'is_motion_mode_switchable', 'use_ref_frame_mvs', 'disable_frame_end_update_cdf', 'allow_warped_motion', 'reduced_tx_set', 'reference_select', 'skip_mode_present', 'delta_q_present', 'delta_lf_present', 'delta_lf_multi', 'segmentation_enabled', 'segmentation_update_map', 'segmentation_temporal_update', 'segmentation_update_data', 'UsesLr', 'usesChromaLr', 'apply_grain', 'reserved']
_member_info_ = {
    'error_resilient_mode': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'disable_cdf_update': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'use_superres': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'render_and_frame_size_different': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'allow_screen_content_tools': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'is_filter_switchable': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'force_integer_mv': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'frame_size_override_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'buffer_removal_time_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'allow_intrabc': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'frame_refs_short_signaling': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'allow_high_precision_mv': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'is_motion_mode_switchable': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'use_ref_frame_mvs': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'disable_frame_end_update_cdf': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'allow_warped_motion': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reduced_tx_set': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reference_select': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'skip_mode_present': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'delta_q_present': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'delta_lf_present': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'delta_lf_multi': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'segmentation_enabled': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'segmentation_update_map': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'segmentation_temporal_update': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'segmentation_update_data': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'UsesLr': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'usesChromaLr': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'apply_grain': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 3,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
