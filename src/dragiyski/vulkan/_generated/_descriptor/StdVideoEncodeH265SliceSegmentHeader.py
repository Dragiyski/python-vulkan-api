from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoEncodeH265SliceSegmentHeader'
_member_list_ = ['flags', 'slice_type', 'slice_segment_address', 'collocated_ref_idx', 'MaxNumMergeCand', 'slice_cb_qp_offset', 'slice_cr_qp_offset', 'slice_beta_offset_div2', 'slice_tc_offset_div2', 'slice_act_y_qp_offset', 'slice_act_cb_qp_offset', 'slice_act_cr_qp_offset', 'slice_qp_delta', 'reserved1', 'pWeightTable']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoEncodeH265SliceSegmentHeaderFlags'),
        'type_name': 'StdVideoEncodeH265SliceSegmentHeaderFlags',
        'structure': 'StdVideoEncodeH265SliceSegmentHeaderFlags',
        'is_string': False,
    },
    'slice_type': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265SliceType',
        'enum': 'StdVideoH265SliceType',
        'is_string': False,
    },
    'slice_segment_address': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'collocated_ref_idx': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'MaxNumMergeCand': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'slice_cb_qp_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_cr_qp_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_beta_offset_div2': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_tc_offset_div2': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_act_y_qp_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_act_cb_qp_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_act_cr_qp_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'slice_qp_delta': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'pWeightTable': {
        'type': CPointerType(CComplexType('StdVideoEncodeH265WeightTable')),
        'type_name': 'StdVideoEncodeH265WeightTable',
        'structure': 'StdVideoEncodeH265WeightTable',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoEncodeH265SliceSegmentHeaderFlags',
    'StdVideoEncodeH265WeightTable',
}
_included_in_ = {
    'VkVideoEncodeH265NaluSliceSegmentInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
