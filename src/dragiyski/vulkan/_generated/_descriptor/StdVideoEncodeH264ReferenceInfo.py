from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264ReferenceInfo'
_member_list_ = ['flags', 'primary_pic_type', 'FrameNum', 'PicOrderCnt', 'long_term_pic_num', 'long_term_frame_idx', 'temporal_id']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH264ReferenceInfoFlags'),
        'type_name': 'StdVideoEncodeH264ReferenceInfoFlags',
        'structure': 'StdVideoEncodeH264ReferenceInfoFlags',
        'is_string': False,
    },
    'primary_pic_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264PictureType',
        'enum': 'StdVideoH264PictureType',
        'is_string': False,
    },
    'FrameNum': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'PicOrderCnt': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'long_term_pic_num': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'long_term_frame_idx': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'temporal_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH264ReferenceInfoFlags',
}
_included_in_ = {
    'VkVideoEncodeH264DpbSlotInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
