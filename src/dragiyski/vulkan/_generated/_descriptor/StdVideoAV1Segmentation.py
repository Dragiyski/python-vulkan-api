from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1Segmentation'
_member_list_ = ['FeatureEnabled', 'FeatureData']
_member_info_ = {
    'FeatureEnabled': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'FeatureData': {
        'type': CArrayType(CArrayType(CIntType('c_int16'), 8), 8),
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
