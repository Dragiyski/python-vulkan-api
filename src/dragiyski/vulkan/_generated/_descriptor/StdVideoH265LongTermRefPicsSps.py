from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265LongTermRefPicsSps'
_member_list_ = ['used_by_curr_pic_lt_sps_flag', 'lt_ref_pic_poc_lsb_sps']
_member_info_ = {
    'used_by_curr_pic_lt_sps_flag': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'lt_ref_pic_poc_lsb_sps': {
        'type': CArrayType(CIntType('c_uint32'), 32),
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
