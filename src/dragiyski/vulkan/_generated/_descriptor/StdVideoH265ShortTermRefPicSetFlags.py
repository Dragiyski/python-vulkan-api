from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265ShortTermRefPicSetFlags'
_member_list_ = ['inter_ref_pic_set_prediction_flag', 'delta_rps_sign']
_member_info_ = {
    'inter_ref_pic_set_prediction_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'delta_rps_sign': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265ShortTermRefPicSet',
}
_input_of_ = set()
_output_of_ = set()
