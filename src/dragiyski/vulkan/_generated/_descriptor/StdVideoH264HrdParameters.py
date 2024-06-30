from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264HrdParameters'
_member_list_ = ['cpb_cnt_minus1', 'bit_rate_scale', 'cpb_size_scale', 'reserved1', 'bit_rate_value_minus1', 'cpb_size_value_minus1', 'cbr_flag', 'initial_cpb_removal_delay_length_minus1', 'cpb_removal_delay_length_minus1', 'dpb_output_delay_length_minus1', 'time_offset_length']
_member_info_ = {
    'cpb_cnt_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'bit_rate_scale': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cpb_size_scale': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'bit_rate_value_minus1': {
        'type': CArrayType(CIntType('c_uint32'), 32),
        'is_string': False,
    },
    'cpb_size_value_minus1': {
        'type': CArrayType(CIntType('c_uint32'), 32),
        'is_string': False,
    },
    'cbr_flag': {
        'type': CArrayType(CIntType('c_uint8'), 32),
        'is_string': False,
    },
    'initial_cpb_removal_delay_length_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'cpb_removal_delay_length_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'dpb_output_delay_length_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'time_offset_length': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH264SequenceParameterSetVui',
}
_input_of_ = set()
_output_of_ = set()
