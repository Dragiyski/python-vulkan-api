from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265SpsVuiFlags'
_member_list_ = ['aspect_ratio_info_present_flag', 'overscan_info_present_flag', 'overscan_appropriate_flag', 'video_signal_type_present_flag', 'video_full_range_flag', 'colour_description_present_flag', 'chroma_loc_info_present_flag', 'neutral_chroma_indication_flag', 'field_seq_flag', 'frame_field_info_present_flag', 'default_display_window_flag', 'vui_timing_info_present_flag', 'vui_poc_proportional_to_timing_flag', 'vui_hrd_parameters_present_flag', 'bitstream_restriction_flag', 'tiles_fixed_structure_flag', 'motion_vectors_over_pic_boundaries_flag', 'restricted_ref_pic_lists_flag']
_member_info_ = {
    'aspect_ratio_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'overscan_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'overscan_appropriate_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'video_signal_type_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'video_full_range_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'colour_description_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'chroma_loc_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'neutral_chroma_indication_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'field_seq_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'frame_field_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'default_display_window_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vui_timing_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vui_poc_proportional_to_timing_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vui_hrd_parameters_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'bitstream_restriction_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'tiles_fixed_structure_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'motion_vectors_over_pic_boundaries_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'restricted_ref_pic_lists_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265SequenceParameterSetVui',
}
_input_of_ = set()
_output_of_ = set()
