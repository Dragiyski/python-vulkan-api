from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264PpsFlags'
_member_list_ = ['transform_8x8_mode_flag', 'redundant_pic_cnt_present_flag', 'constrained_intra_pred_flag', 'deblocking_filter_control_present_flag', 'weighted_pred_flag', 'bottom_field_pic_order_in_frame_present_flag', 'entropy_coding_mode_flag', 'pic_scaling_matrix_present_flag']
_member_info_ = {
    'transform_8x8_mode_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'redundant_pic_cnt_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'constrained_intra_pred_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'deblocking_filter_control_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'weighted_pred_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'bottom_field_pic_order_in_frame_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'entropy_coding_mode_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pic_scaling_matrix_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH264PictureParameterSet',
}
_input_of_ = set()
_output_of_ = set()
