from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265LongTermRefPics'
_member_list_ = ['num_long_term_sps', 'num_long_term_pics', 'lt_idx_sps', 'poc_lsb_lt', 'used_by_curr_pic_lt_flag', 'delta_poc_msb_present_flag', 'delta_poc_msb_cycle_lt']
_member_info_ = {
    'num_long_term_sps': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_long_term_pics': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'lt_idx_sps': {
        'type': CArrayType(CIntType('c_uint8'), 32),
        'is_string': False,
    },
    'poc_lsb_lt': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
    'used_by_curr_pic_lt_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'delta_poc_msb_present_flag': {
        'type': CArrayType(CIntType('c_uint8'), 48),
        'is_string': False,
    },
    'delta_poc_msb_cycle_lt': {
        'type': CArrayType(CIntType('c_uint8'), 48),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoEncodeH265PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
