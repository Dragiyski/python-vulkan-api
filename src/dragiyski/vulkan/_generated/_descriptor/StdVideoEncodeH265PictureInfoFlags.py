from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265PictureInfoFlags'
_member_list_ = ['is_reference', 'IrapPicFlag', 'used_for_long_term_reference', 'discardable_flag', 'cross_layer_bla_flag', 'pic_output_flag', 'no_output_of_prior_pics_flag', 'short_term_ref_pic_set_sps_flag', 'slice_temporal_mvp_enabled_flag', 'reserved']
_member_info_ = {
    'is_reference': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'IrapPicFlag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'used_for_long_term_reference': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'discardable_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'cross_layer_bla_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'pic_output_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'no_output_of_prior_pics_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'short_term_ref_pic_set_sps_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'slice_temporal_mvp_enabled_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 23,
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
