from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264SpsFlags'
_member_list_ = ['constraint_set0_flag', 'constraint_set1_flag', 'constraint_set2_flag', 'constraint_set3_flag', 'constraint_set4_flag', 'constraint_set5_flag', 'direct_8x8_inference_flag', 'mb_adaptive_frame_field_flag', 'frame_mbs_only_flag', 'delta_pic_order_always_zero_flag', 'separate_colour_plane_flag', 'gaps_in_frame_num_value_allowed_flag', 'qpprime_y_zero_transform_bypass_flag', 'frame_cropping_flag', 'seq_scaling_matrix_present_flag', 'vui_parameters_present_flag']
_member_info_ = {
    'constraint_set0_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'constraint_set1_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'constraint_set2_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'constraint_set3_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'constraint_set4_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'constraint_set5_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'direct_8x8_inference_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'mb_adaptive_frame_field_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'frame_mbs_only_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'delta_pic_order_always_zero_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'separate_colour_plane_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'gaps_in_frame_num_value_allowed_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'qpprime_y_zero_transform_bypass_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'frame_cropping_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'seq_scaling_matrix_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vui_parameters_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH264SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
