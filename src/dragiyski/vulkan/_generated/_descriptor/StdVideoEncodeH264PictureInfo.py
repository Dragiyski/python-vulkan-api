from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264PictureInfo'
_member_list_ = ['flags', 'seq_parameter_set_id', 'pic_parameter_set_id', 'idr_pic_id', 'primary_pic_type', 'frame_num', 'PicOrderCnt', 'temporal_id', 'reserved1', 'pRefLists']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH264PictureInfoFlags'),
        'type_name': 'StdVideoEncodeH264PictureInfoFlags',
        'structure': 'StdVideoEncodeH264PictureInfoFlags',
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
    'idr_pic_id': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'primary_pic_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264PictureType',
        'enum': 'StdVideoH264PictureType',
        'is_string': False,
    },
    'frame_num': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'PicOrderCnt': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'temporal_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CArrayType(CIntType('c_uint8'), 3),
        'is_string': False,
    },
    'pRefLists': {
        'type': CPointerType(CComplexType('StdVideoEncodeH264ReferenceListsInfo')),
        'type_name': 'StdVideoEncodeH264ReferenceListsInfo',
        'structure': 'StdVideoEncodeH264ReferenceListsInfo',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH264PictureInfoFlags',
    'StdVideoEncodeH264ReferenceListsInfo',
}
_included_in_ = {
    'VkVideoEncodeH264PictureInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
