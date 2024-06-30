from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeH264ReferenceInfo'
_member_list_ = ['flags', 'FrameNum', 'reserved', 'PicOrderCnt']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoDecodeH264ReferenceInfoFlags'),
        'type_name': 'StdVideoDecodeH264ReferenceInfoFlags',
        'structure': 'StdVideoDecodeH264ReferenceInfoFlags',
        'is_string': False,
    },
    'FrameNum': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'reserved': {
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
    'StdVideoDecodeH264ReferenceInfoFlags',
}
_included_in_ = {
    'VkVideoDecodeH264DpbSlotInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
