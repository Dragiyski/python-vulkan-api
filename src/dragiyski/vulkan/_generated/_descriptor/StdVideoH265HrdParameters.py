from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265HrdParameters'
_member_list_ = ['flags', 'tick_divisor_minus2', 'du_cpb_removal_delay_increment_length_minus1', 'dpb_output_delay_du_length_minus1', 'bit_rate_scale', 'cpb_size_scale', 'cpb_size_du_scale', 'initial_cpb_removal_delay_length_minus1', 'au_cpb_removal_delay_length_minus1', 'dpb_output_delay_length_minus1', 'cpb_cnt_minus1', 'elemental_duration_in_tc_minus1', 'reserved', 'pSubLayerHrdParametersNal', 'pSubLayerHrdParametersVcl']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH265HrdFlags'),
        'type_name': 'StdVideoH265HrdFlags',
        'structure': 'StdVideoH265HrdFlags',
        'is_string': False,
    },
    'tick_divisor_minus2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'du_cpb_removal_delay_increment_length_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'dpb_output_delay_du_length_minus1': {
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
    'cpb_size_du_scale': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'initial_cpb_removal_delay_length_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'au_cpb_removal_delay_length_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'dpb_output_delay_length_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cpb_cnt_minus1': {
        'type': CArrayType(CIntType('c_uint8'), 7),
        'is_string': False,
    },
    'elemental_duration_in_tc_minus1': {
        'type': CArrayType(CIntType('c_uint16'), 7),
        'is_string': False,
    },
    'reserved': {
        'type': CArrayType(CIntType('c_uint16'), 3),
        'is_string': False,
    },
    'pSubLayerHrdParametersNal': {
        'type': CPointerType(CComplexType('StdVideoH265SubLayerHrdParameters')),
        'type_name': 'StdVideoH265SubLayerHrdParameters',
        'structure': 'StdVideoH265SubLayerHrdParameters',
        'is_string': False,
    },
    'pSubLayerHrdParametersVcl': {
        'type': CPointerType(CComplexType('StdVideoH265SubLayerHrdParameters')),
        'type_name': 'StdVideoH265SubLayerHrdParameters',
        'structure': 'StdVideoH265SubLayerHrdParameters',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoH265HrdFlags',
    'StdVideoH265SubLayerHrdParameters',
}
_included_in_ = {
    'StdVideoH265SequenceParameterSetVui',
    'StdVideoH265VideoParameterSet',
}
_input_of_ = set()
_output_of_ = set()
