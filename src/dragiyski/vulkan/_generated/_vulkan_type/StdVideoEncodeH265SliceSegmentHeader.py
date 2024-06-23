import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265SliceSegmentHeaderFlags import CType as StdVideoEncodeH265SliceSegmentHeaderFlags
from .StdVideoEncodeH265WeightTable import CType as StdVideoEncodeH265WeightTable

CType._fields_ = [
    ('flags', StdVideoEncodeH265SliceSegmentHeaderFlags),
    ('slice_type', ctypes.c_int),
    ('slice_segment_address', ctypes.c_uint32),
    ('collocated_ref_idx', ctypes.c_uint8),
    ('MaxNumMergeCand', ctypes.c_uint8),
    ('slice_cb_qp_offset', ctypes.c_int8),
    ('slice_cr_qp_offset', ctypes.c_int8),
    ('slice_beta_offset_div2', ctypes.c_int8),
    ('slice_tc_offset_div2', ctypes.c_int8),
    ('slice_act_y_qp_offset', ctypes.c_int8),
    ('slice_act_cb_qp_offset', ctypes.c_int8),
    ('slice_act_cr_qp_offset', ctypes.c_int8),
    ('slice_qp_delta', ctypes.c_int8),
    ('reserved1', ctypes.c_uint16),
    ('pWeightTable', ctypes.POINTER(StdVideoEncodeH265WeightTable)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH265SliceSegmentHeaderFlags',
        'StdVideoEncodeH265WeightTable',
    },
    'included_in': {
        'VkVideoEncodeH265NaluSliceSegmentInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH265SliceSegmentHeaderFlags'},
        'slice_type': {'python_name': ['slice', 'type'], 'type': 'StdVideoH265SliceType'},
        'slice_segment_address': {'python_name': ['slice', 'segment', 'address']},
        'collocated_ref_idx': {'python_name': ['collocated', 'ref', 'idx']},
        'MaxNumMergeCand': {'python_name': ['max', 'num', 'merge', 'cand']},
        'slice_cb_qp_offset': {'python_name': ['slice', 'cb', 'qp', 'offset']},
        'slice_cr_qp_offset': {'python_name': ['slice', 'cr', 'qp', 'offset']},
        'slice_beta_offset_div2': {'python_name': ['slice', 'beta', 'offset', 'div2']},
        'slice_tc_offset_div2': {'python_name': ['slice', 'tc', 'offset', 'div2']},
        'slice_act_y_qp_offset': {'python_name': ['slice', 'act', 'y', 'qp', 'offset']},
        'slice_act_cb_qp_offset': {'python_name': ['slice', 'act', 'cb', 'qp', 'offset']},
        'slice_act_cr_qp_offset': {'python_name': ['slice', 'act', 'cr', 'qp', 'offset']},
        'slice_qp_delta': {'python_name': ['slice', 'qp', 'delta']},
        'reserved1': {'python_name': ['reserved1']},
        'pWeightTable': {'python_name': ['p', 'weight', 'table'], 'type': 'StdVideoEncodeH265WeightTable'},
    }
}
