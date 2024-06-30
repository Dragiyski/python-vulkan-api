from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeH265PictureInfo'
_member_list_ = ['flags', 'sps_video_parameter_set_id', 'pps_seq_parameter_set_id', 'pps_pic_parameter_set_id', 'NumDeltaPocsOfRefRpsIdx', 'PicOrderCntVal', 'NumBitsForSTRefPicSetInSlice', 'reserved', 'RefPicSetStCurrBefore', 'RefPicSetStCurrAfter', 'RefPicSetLtCurr']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoDecodeH265PictureInfoFlags'),
        'type_name': 'StdVideoDecodeH265PictureInfoFlags',
        'structure': 'StdVideoDecodeH265PictureInfoFlags',
        'is_string': False,
    },
    'sps_video_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pps_seq_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pps_pic_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'NumDeltaPocsOfRefRpsIdx': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'PicOrderCntVal': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'NumBitsForSTRefPicSetInSlice': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'reserved': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'RefPicSetStCurrBefore': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'RefPicSetStCurrAfter': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
    'RefPicSetLtCurr': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoDecodeH265PictureInfoFlags',
}
_included_in_ = {
    'VkVideoDecodeH265PictureInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
