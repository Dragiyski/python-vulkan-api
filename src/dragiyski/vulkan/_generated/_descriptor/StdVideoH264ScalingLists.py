from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264ScalingLists'
_member_list_ = ['scaling_list_present_mask', 'use_default_scaling_matrix_mask', 'ScalingList4x4', 'ScalingList8x8']
_member_info_ = {
    'scaling_list_present_mask': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'use_default_scaling_matrix_mask': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'ScalingList4x4': {
        'type': CArrayType(CArrayType(CIntType('c_uint8'), 16), 6),
        'is_string': False,
    },
    'ScalingList8x8': {
        'type': CArrayType(CArrayType(CIntType('c_uint8'), 64), 6),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH264PictureParameterSet',
    'StdVideoH264SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
