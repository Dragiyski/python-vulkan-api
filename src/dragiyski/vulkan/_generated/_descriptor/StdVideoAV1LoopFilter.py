from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1LoopFilter'
_member_list_ = ['flags', 'loop_filter_level', 'loop_filter_sharpness', 'update_ref_delta', 'loop_filter_ref_deltas', 'update_mode_delta', 'loop_filter_mode_deltas']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoAV1LoopFilterFlags'),
        'type_name': 'StdVideoAV1LoopFilterFlags',
        'structure': 'StdVideoAV1LoopFilterFlags',
        'is_string': False,
    },
    'loop_filter_level': {
        'type': CArrayType(CIntType('c_uint8'), 4),
        'is_string': False,
    },
    'loop_filter_sharpness': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'update_ref_delta': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'loop_filter_ref_deltas': {
        'type': CArrayType(CIntType('c_int8'), 8),
        'is_string': False,
    },
    'update_mode_delta': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'loop_filter_mode_deltas': {
        'type': CArrayType(CIntType('c_int8'), 2),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1LoopFilterFlags',
}
_included_in_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
