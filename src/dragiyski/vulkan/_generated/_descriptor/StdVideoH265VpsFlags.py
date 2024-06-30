from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265VpsFlags'
_member_list_ = ['vps_temporal_id_nesting_flag', 'vps_sub_layer_ordering_info_present_flag', 'vps_timing_info_present_flag', 'vps_poc_proportional_to_timing_flag']
_member_info_ = {
    'vps_temporal_id_nesting_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vps_sub_layer_ordering_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vps_timing_info_present_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'vps_poc_proportional_to_timing_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265VideoParameterSet',
}
_input_of_ = set()
_output_of_ = set()
