from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265WeightTableFlags'
_member_list_ = ['luma_weight_l0_flag', 'chroma_weight_l0_flag', 'luma_weight_l1_flag', 'chroma_weight_l1_flag']
_member_info_ = {
    'luma_weight_l0_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'chroma_weight_l0_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'luma_weight_l1_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'chroma_weight_l1_flag': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoEncodeH265WeightTable',
}
_input_of_ = set()
_output_of_ = set()
