from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264PictureInfoFlags'
_member_list_ = ['IdrPicFlag', 'is_reference', 'no_output_of_prior_pics_flag', 'long_term_reference_flag', 'adaptive_ref_pic_marking_mode_flag', 'reserved']
_member_info_ = {
    'IdrPicFlag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'is_reference': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'no_output_of_prior_pics_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'long_term_reference_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'adaptive_ref_pic_marking_mode_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint32'),
        'bitsize': 27,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoEncodeH264PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
