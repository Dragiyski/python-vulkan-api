from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265ShortTermRefPicSet'
_member_list_ = ['flags', 'delta_idx_minus1', 'use_delta_flag', 'abs_delta_rps_minus1', 'used_by_curr_pic_flag', 'used_by_curr_pic_s0_flag', 'used_by_curr_pic_s1_flag', 'reserved1', 'reserved2', 'reserved3', 'num_negative_pics', 'num_positive_pics', 'delta_poc_s0_minus1', 'delta_poc_s1_minus1']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH265ShortTermRefPicSetFlags'),
        'type_name': 'StdVideoH265ShortTermRefPicSetFlags',
        'structure': 'StdVideoH265ShortTermRefPicSetFlags',
        'is_string': False,
    },
    'delta_idx_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'use_delta_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'abs_delta_rps_minus1': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'used_by_curr_pic_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'used_by_curr_pic_s0_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'used_by_curr_pic_s1_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'reserved2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved3': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_negative_pics': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_positive_pics': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'delta_poc_s0_minus1': {
        'type': CArrayType(CIntType('c_uint16'), 16),
        'is_string': False,
    },
    'delta_poc_s1_minus1': {
        'type': CArrayType(CIntType('c_uint16'), 16),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoH265ShortTermRefPicSetFlags',
}
_included_in_ = {
    'StdVideoEncodeH265PictureInfo',
    'StdVideoH265SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
