from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1GlobalMotion'
_member_list_ = ['GmType', 'gm_params']
_member_info_ = {
    'GmType': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'gm_params': {
        'type': CArrayType(CArrayType(CIntType('c_int32'), 6), 8),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
