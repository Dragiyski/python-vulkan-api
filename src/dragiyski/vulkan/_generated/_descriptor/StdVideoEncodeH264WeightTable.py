from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264WeightTable'
_member_list_ = ['flags', 'luma_log2_weight_denom', 'chroma_log2_weight_denom', 'luma_weight_l0', 'luma_offset_l0', 'chroma_weight_l0', 'chroma_offset_l0', 'luma_weight_l1', 'luma_offset_l1', 'chroma_weight_l1', 'chroma_offset_l1']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH264WeightTableFlags'),
        'type_name': 'StdVideoEncodeH264WeightTableFlags',
        'structure': 'StdVideoEncodeH264WeightTableFlags',
        'is_string': False,
    },
    'luma_log2_weight_denom': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'chroma_log2_weight_denom': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'luma_weight_l0': {
        'type': CArrayType(CIntType('c_int8'), 32),
        'is_string': False,
    },
    'luma_offset_l0': {
        'type': CArrayType(CIntType('c_int8'), 32),
        'is_string': False,
    },
    'chroma_weight_l0': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 32),
        'is_string': False,
    },
    'chroma_offset_l0': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 32),
        'is_string': False,
    },
    'luma_weight_l1': {
        'type': CArrayType(CIntType('c_int8'), 32),
        'is_string': False,
    },
    'luma_offset_l1': {
        'type': CArrayType(CIntType('c_int8'), 32),
        'is_string': False,
    },
    'chroma_weight_l1': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 32),
        'is_string': False,
    },
    'chroma_offset_l1': {
        'type': CArrayType(CArrayType(CIntType('c_int8'), 2), 32),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH264WeightTableFlags',
}
_included_in_ = {
    'StdVideoEncodeH264SliceHeader',
}
_input_of_ = set()
_output_of_ = set()
