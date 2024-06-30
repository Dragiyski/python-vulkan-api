from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoDecodeAV1ReferenceInfo'
_member_list_ = ['flags', 'frame_type', 'RefFrameSignBias', 'OrderHint', 'SavedOrderHints']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoDecodeAV1ReferenceInfoFlags'),
        'type_name': 'StdVideoDecodeAV1ReferenceInfoFlags',
        'structure': 'StdVideoDecodeAV1ReferenceInfoFlags',
        'is_string': False,
    },
    'frame_type': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'RefFrameSignBias': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'OrderHint': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'SavedOrderHints': {
        'type': CArrayType(CIntType('c_uint8'), 8),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoDecodeAV1ReferenceInfoFlags',
}
_included_in_ = {
    'VkVideoDecodeAV1DpbSlotInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
