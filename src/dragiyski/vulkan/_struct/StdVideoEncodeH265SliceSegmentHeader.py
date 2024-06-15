import ctypes, sys

class StdVideoEncodeH265SliceSegmentHeader(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoEncodeH265SliceSegmentHeader

from . import StdVideoEncodeH265WeightTable
from . import StdVideoEncodeH265SliceSegmentHeaderFlags

StdVideoEncodeH265SliceSegmentHeader._fields_ = [
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
