from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeH264PictureInfo'
_member_list_ = ['flags', 'seq_parameter_set_id', 'pic_parameter_set_id', 'reserved1', 'reserved2', 'frame_num', 'idr_pic_id', 'PicOrderCnt']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoDecodeH264PictureInfoFlags'),
        'type_name': 'StdVideoDecodeH264PictureInfoFlags',
        'structure': 'StdVideoDecodeH264PictureInfoFlags',
        'is_string': False,
    },
    'seq_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pic_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'frame_num': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'idr_pic_id': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'PicOrderCnt': {
        'type': CArrayType(CIntType('c_int32'), 2),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoDecodeH264PictureInfoFlags',
}
_included_in_ = {
    'VkVideoDecodeH264PictureInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
