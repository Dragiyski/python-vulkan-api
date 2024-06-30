from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265PictureInfo'
_member_list_ = ['flags', 'pic_type', 'sps_video_parameter_set_id', 'pps_seq_parameter_set_id', 'pps_pic_parameter_set_id', 'short_term_ref_pic_set_idx', 'PicOrderCntVal', 'TemporalId', 'reserved1', 'pRefLists', 'pShortTermRefPicSet', 'pLongTermRefPics']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH265PictureInfoFlags'),
        'type_name': 'StdVideoEncodeH265PictureInfoFlags',
        'structure': 'StdVideoEncodeH265PictureInfoFlags',
        'is_string': False,
    },
    'pic_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265PictureType',
        'enum': 'StdVideoH265PictureType',
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
    'short_term_ref_pic_set_idx': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'PicOrderCntVal': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'TemporalId': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CArrayType(CIntType('c_uint8'), 7),
        'is_string': False,
    },
    'pRefLists': {
        'type': CPointerType(CComplexType('StdVideoEncodeH265ReferenceListsInfo')),
        'type_name': 'StdVideoEncodeH265ReferenceListsInfo',
        'structure': 'StdVideoEncodeH265ReferenceListsInfo',
        'is_string': False,
    },
    'pShortTermRefPicSet': {
        'type': CPointerType(CComplexType('StdVideoH265ShortTermRefPicSet')),
        'type_name': 'StdVideoH265ShortTermRefPicSet',
        'structure': 'StdVideoH265ShortTermRefPicSet',
        'is_string': False,
    },
    'pLongTermRefPics': {
        'type': CPointerType(CComplexType('StdVideoEncodeH265LongTermRefPics')),
        'type_name': 'StdVideoEncodeH265LongTermRefPics',
        'structure': 'StdVideoEncodeH265LongTermRefPics',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265LongTermRefPics',
    'StdVideoEncodeH265PictureInfoFlags',
    'StdVideoEncodeH265ReferenceListsInfo',
    'StdVideoH265ShortTermRefPicSet',
}
_included_in_ = {
    'VkVideoEncodeH265PictureInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
