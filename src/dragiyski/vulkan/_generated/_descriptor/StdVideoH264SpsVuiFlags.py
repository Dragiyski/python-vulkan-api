from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264SpsVuiFlags'
_member_list_ = ['aspect_ratio_info_present_flag', 'overscan_info_present_flag', 'overscan_appropriate_flag', 'video_signal_type_present_flag', 'video_full_range_flag', 'color_description_present_flag', 'chroma_loc_info_present_flag', 'timing_info_present_flag', 'fixed_frame_rate_flag', 'bitstream_restriction_flag', 'nal_hrd_parameters_present_flag', 'vcl_hrd_parameters_present_flag']
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
    'color_description_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'chroma_loc_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'timing_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'fixed_frame_rate_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'bitstream_restriction_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'nal_hrd_parameters_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vcl_hrd_parameters_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH264SequenceParameterSetVui',
}
_input_of_ = set()
_output_of_ = set()
