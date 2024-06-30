from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265ReferenceInfo'
_member_list_ = ['flags', 'pic_type', 'PicOrderCntVal', 'TemporalId']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH265ReferenceInfoFlags'),
        'type_name': 'StdVideoEncodeH265ReferenceInfoFlags',
        'structure': 'StdVideoEncodeH265ReferenceInfoFlags',
        'is_string': False,
    },
    'pic_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265PictureType',
        'enum': 'StdVideoH265PictureType',
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
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265ReferenceInfoFlags',
}
_included_in_ = {
    'VkVideoEncodeH265DpbSlotInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
