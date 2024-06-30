from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH264SliceHeader'
_member_list_ = ['flags', 'first_mb_in_slice', 'slice_type', 'slice_alpha_c0_offset_div2', 'slice_beta_offset_div2', 'slice_qp_delta', 'reserved1', 'cabac_init_idc', 'disable_deblocking_filter_idc', 'pWeightTable']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH264SliceHeaderFlags'),
        'type_name': 'StdVideoEncodeH264SliceHeaderFlags',
        'structure': 'StdVideoEncodeH264SliceHeaderFlags',
        'is_string': False,
    },
    'first_mb_in_slice': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'slice_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264SliceType',
        'enum': 'StdVideoH264SliceType',
        'is_string': False,
    },
    'slice_alpha_c0_offset_div2': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_beta_offset_div2': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_qp_delta': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cabac_init_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264CabacInitIdc',
        'enum': 'StdVideoH264CabacInitIdc',
        'is_string': False,
    },
    'disable_deblocking_filter_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264DisableDeblockingFilterIdc',
        'enum': 'StdVideoH264DisableDeblockingFilterIdc',
        'is_string': False,
    },
    'pWeightTable': {
        'type': CPointerType(CComplexType('StdVideoEncodeH264WeightTable')),
        'type_name': 'StdVideoEncodeH264WeightTable',
        'structure': 'StdVideoEncodeH264WeightTable',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH264SliceHeaderFlags',
    'StdVideoEncodeH264WeightTable',
}
_included_in_ = {
    'VkVideoEncodeH264NaluSliceInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
