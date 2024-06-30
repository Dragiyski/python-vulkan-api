from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265DecPicBufMgr'
_member_list_ = ['max_latency_increase_plus1', 'max_dec_pic_buffering_minus1', 'max_num_reorder_pics']
_member_info_ = {
    'max_latency_increase_plus1': {
        'type': CArrayType(CIntType('c_uint32'), 7),
        'is_string': False,
    },
    'max_dec_pic_buffering_minus1': {
        'type': CArrayType(CIntType('c_uint8'), 7),
        'is_string': False,
    },
    'max_num_reorder_pics': {
        'type': CArrayType(CIntType('c_uint8'), 7),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265SequenceParameterSet',
    'StdVideoH265VideoParameterSet',
}
_input_of_ = set()
_output_of_ = set()
