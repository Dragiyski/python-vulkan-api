from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1Quantization'
_member_list_ = ['flags', 'base_q_idx', 'DeltaQYDc', 'DeltaQUDc', 'DeltaQUAc', 'DeltaQVDc', 'DeltaQVAc', 'qm_y', 'qm_u', 'qm_v']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoAV1QuantizationFlags'),
        'type_name': 'StdVideoAV1QuantizationFlags',
        'structure': 'StdVideoAV1QuantizationFlags',
        'is_string': False,
    },
    'base_q_idx': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'DeltaQYDc': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'DeltaQUDc': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'DeltaQUAc': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'DeltaQVDc': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'DeltaQVAc': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'qm_y': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'qm_u': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'qm_v': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1QuantizationFlags',
}
_included_in_ = {
    'StdVideoDecodeAV1PictureInfo',
}
_input_of_ = set()
_output_of_ = set()
