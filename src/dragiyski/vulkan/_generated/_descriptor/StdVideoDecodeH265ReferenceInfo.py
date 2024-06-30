from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeH265ReferenceInfo'
_member_list_ = ['flags', 'PicOrderCntVal']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoDecodeH265ReferenceInfoFlags'),
        'type_name': 'StdVideoDecodeH265ReferenceInfoFlags',
        'structure': 'StdVideoDecodeH265ReferenceInfoFlags',
        'is_string': False,
    },
    'PicOrderCntVal': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoDecodeH265ReferenceInfoFlags',
}
_included_in_ = {
    'VkVideoDecodeH265DpbSlotInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
