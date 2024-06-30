from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265WeightTable'
_member_list_ = ['flags', 'luma_log2_weight_denom', 'delta_chroma_log2_weight_denom', 'delta_luma_weight_l0', 'luma_offset_l0', 'delta_chroma_weight_l0', 'delta_chroma_offset_l0', 'delta_luma_weight_l1', 'luma_offset_l1', 'delta_chroma_weight_l1', 'delta_chroma_offset_l1']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH265WeightTableFlags'),
        'type_name': 'StdVideoEncodeH265WeightTableFlags',
        'structure': 'StdVideoEncodeH265WeightTableFlags',
        'is_string': False,
    },
    'luma_log2_weight_denom': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'delta_chroma_log2_weight_denom': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'delta_luma_weight_l0': {
        'type': CArrayType(CIntType('c_int8'), 15),
        'is_string': False,
    },
    'luma_offset_l0': {
        'type': CArrayType(CIntType('c_int8'), 15),
        'is_string': False,
    },
    'delta_chroma_weight_l0': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 15),
        'is_string': False,
    },
    'delta_chroma_offset_l0': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 15),
        'is_string': False,
    },
    'delta_luma_weight_l1': {
        'type': CArrayType(CIntType('c_int8'), 15),
        'is_string': False,
    },
    'luma_offset_l1': {
        'type': CArrayType(CIntType('c_int8'), 15),
        'is_string': False,
    },
    'delta_chroma_weight_l1': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 15),
        'is_string': False,
    },
    'delta_chroma_offset_l1': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 15),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265WeightTableFlags',
}
_included_in_ = {
    'StdVideoEncodeH265SliceSegmentHeader',
}
_input_of_ = set()
_output_of_ = set()
