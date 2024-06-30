from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeH265PictureInfoFlags'
_member_list_ = ['IrapPicFlag', 'IdrPicFlag', 'IsReference', 'short_term_ref_pic_set_sps_flag']
_member_info_ = {
    'IrapPicFlag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'IdrPicFlag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'IsReference': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
    'short_term_ref_pic_set_sps_flag': {
        'type': CIntType('c_uint32'),
        'bitsize': 1,
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeH265PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
