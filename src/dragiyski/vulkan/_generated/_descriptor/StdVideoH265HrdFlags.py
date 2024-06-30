from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265HrdFlags'
_member_list_ = ['nal_hrd_parameters_present_flag', 'vcl_hrd_parameters_present_flag', 'sub_pic_hrd_params_present_flag', 'sub_pic_cpb_params_in_pic_timing_sei_flag', 'fixed_pic_rate_general_flag', 'fixed_pic_rate_within_cvs_flag', 'low_delay_hrd_flag']
_member_info_ = {
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
    'sub_pic_hrd_params_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'sub_pic_cpb_params_in_pic_timing_sei_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'fixed_pic_rate_general_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 8,
        'is_string': False,
    },
    'fixed_pic_rate_within_cvs_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 8,
        'is_string': False,
    },
    'low_delay_hrd_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 8,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265HrdParameters',
}
_input_of_ = set()
_output_of_ = set()
