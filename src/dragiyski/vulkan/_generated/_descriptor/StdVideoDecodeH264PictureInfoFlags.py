from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeH264PictureInfoFlags'
_member_list_ = ['field_pic_flag', 'is_intra', 'IdrPicFlag', 'bottom_field_flag', 'is_reference', 'complementary_field_pair']
_member_info_ = {
    'field_pic_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'is_intra': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'IdrPicFlag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'bottom_field_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'is_reference': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'complementary_field_pair': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeH264PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
