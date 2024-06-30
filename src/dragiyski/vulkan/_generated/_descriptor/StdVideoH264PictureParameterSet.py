from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264PictureParameterSet'
_member_list_ = ['flags', 'seq_parameter_set_id', 'pic_parameter_set_id', 'num_ref_idx_l0_default_active_minus1', 'num_ref_idx_l1_default_active_minus1', 'weighted_bipred_idc', 'pic_init_qp_minus26', 'pic_init_qs_minus26', 'chroma_qp_index_offset', 'second_chroma_qp_index_offset', 'pScalingLists']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH264PpsFlags'),
        'type_name': 'StdVideoH264PpsFlags',
        'structure': 'StdVideoH264PpsFlags',
        'is_string': False,
    },
    'seq_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pic_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_ref_idx_l0_default_active_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_ref_idx_l1_default_active_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'weighted_bipred_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264WeightedBipredIdc',
        'enum': 'StdVideoH264WeightedBipredIdc',
        'is_string': False,
    },
    'pic_init_qp_minus26': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pic_init_qs_minus26': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'chroma_qp_index_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'second_chroma_qp_index_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pScalingLists': {
        'type': CPointerType(CComplexType('StdVideoH264ScalingLists')),
        'type_name': 'StdVideoH264ScalingLists',
        'structure': 'StdVideoH264ScalingLists',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoH264PpsFlags',
    'StdVideoH264ScalingLists',
}
_included_in_ = {
    'VkVideoDecodeH264SessionParametersAddInfoKHR',
    'VkVideoEncodeH264SessionParametersAddInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
