from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265SubLayerHrdParameters'
_member_list_ = ['bit_rate_value_minus1', 'cpb_size_value_minus1', 'cpb_size_du_value_minus1', 'bit_rate_du_value_minus1', 'cbr_flag']
_member_info_ = {
    'bit_rate_value_minus1': {
        'type': CArrayType(CIntType('c_uint32'), 32),
        'is_string': False,
    },
    'cpb_size_value_minus1': {
        'type': CArrayType(CIntType('c_uint32'), 32),
        'is_string': False,
    },
    'cpb_size_du_value_minus1': {
        'type': CArrayType(CIntType('c_uint32'), 32),
        'is_string': False,
    },
    'bit_rate_du_value_minus1': {
        'type': CArrayType(CIntType('c_uint32'), 32),
        'is_string': False,
    },
    'cbr_flag': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265HrdParameters',
}
_input_of_ = set()
_output_of_ = set()
