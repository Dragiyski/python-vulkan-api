import ctypes

class StdVideoEncodeH265SliceSegmentHeader(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'flags': 'flags',
        'slice_type': 'slice_type',
        'slice_segment_address': 'slice_segment_address',
        'collocated_ref_idx': 'collocated_ref_idx',
        'MaxNumMergeCand': 'max_num_merge_cand',
        'slice_cb_qp_offset': 'slice_cb_qp_offset',
        'slice_cr_qp_offset': 'slice_cr_qp_offset',
        'slice_beta_offset_div2': 'slice_beta_offset_div2',
        'slice_tc_offset_div2': 'slice_tc_offset_div2',
        'slice_act_y_qp_offset': 'slice_act_y_qp_offset',
        'slice_act_cb_qp_offset': 'slice_act_cb_qp_offset',
        'slice_act_cr_qp_offset': 'slice_act_cr_qp_offset',
        'slice_qp_delta': 'slice_qp_delta',
        'reserved1': 'reserved1',
        'pWeightTable': 'weight_table',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_encode',
    }
    _vk_enum_ = {
        'slice_type': 'StdVideoH265SliceType',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoEncodeH265SliceSegmentHeaderFlags import StdVideoEncodeH265SliceSegmentHeaderFlags
from .StdVideoEncodeH265WeightTable import StdVideoEncodeH265WeightTable

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

StdVideoEncodeH265SliceSegmentHeader._type_ = {
    'flags': StdVideoEncodeH265SliceSegmentHeaderFlags,
    'slice_type': ctypes.c_int,
    'slice_segment_address': ctypes.c_uint32,
    'collocated_ref_idx': ctypes.c_uint8,
    'MaxNumMergeCand': ctypes.c_uint8,
    'slice_cb_qp_offset': ctypes.c_int8,
    'slice_cr_qp_offset': ctypes.c_int8,
    'slice_beta_offset_div2': ctypes.c_int8,
    'slice_tc_offset_div2': ctypes.c_int8,
    'slice_act_y_qp_offset': ctypes.c_int8,
    'slice_act_cb_qp_offset': ctypes.c_int8,
    'slice_act_cr_qp_offset': ctypes.c_int8,
    'slice_qp_delta': ctypes.c_int8,
    'reserved1': ctypes.c_uint16,
    'pWeightTable': ctypes.POINTER(StdVideoEncodeH265WeightTable),
}
