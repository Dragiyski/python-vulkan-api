from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265ScalingLists'
_member_list_ = ['ScalingList4x4', 'ScalingList8x8', 'ScalingList16x16', 'ScalingList32x32', 'ScalingListDCCoef16x16', 'ScalingListDCCoef32x32']
_member_info_ = {
    'ScalingList4x4': {
        'type': CArrayType(CArrayType(CIntType('c_uint8'), 16), 6),
        'is_string': False,
    },
    'ScalingList8x8': {
        'type': CArrayType(CArrayType(CIntType('c_uint8'), 64), 6),
        'is_string': False,
    },
    'ScalingList16x16': {
        'type': CArrayType(CArrayType(CIntType('c_uint8'), 64), 6),
        'is_string': False,
    },
    'ScalingList32x32': {
        'type': CArrayType(CArrayType(CIntType('c_uint8'), 64), 2),
        'is_string': False,
    },
    'ScalingListDCCoef16x16': {
        'type': CArrayType(CIntType('c_uint8'), 6),
        'is_string': False,
    },
    'ScalingListDCCoef32x32': {
        'type': CArrayType(CIntType('c_uint8'), 2),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'StdVideoH265PictureParameterSet',
    'StdVideoH265SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
