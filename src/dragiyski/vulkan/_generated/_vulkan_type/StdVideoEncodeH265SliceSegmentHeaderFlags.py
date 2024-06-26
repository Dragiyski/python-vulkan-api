import ctypes

class StdVideoEncodeH265SliceSegmentHeaderFlags(ctypes.Structure):
    _fields_ = [
        ('first_slice_segment_in_pic_flag', ctypes.c_uint32, 1),
        ('dependent_slice_segment_flag', ctypes.c_uint32, 1),
        ('slice_sao_luma_flag', ctypes.c_uint32, 1),
        ('slice_sao_chroma_flag', ctypes.c_uint32, 1),
        ('num_ref_idx_active_override_flag', ctypes.c_uint32, 1),
        ('mvd_l1_zero_flag', ctypes.c_uint32, 1),
        ('cabac_init_flag', ctypes.c_uint32, 1),
        ('cu_chroma_qp_offset_enabled_flag', ctypes.c_uint32, 1),
        ('deblocking_filter_override_flag', ctypes.c_uint32, 1),
        ('slice_deblocking_filter_disabled_flag', ctypes.c_uint32, 1),
        ('collocated_from_l0_flag', ctypes.c_uint32, 1),
        ('slice_loop_filter_across_slices_enabled_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 20),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoEncodeH265SliceSegmentHeader',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'first_slice_segment_in_pic_flag': 'first_slice_segment_in_pic_flag',
        'dependent_slice_segment_flag': 'dependent_slice_segment_flag',
        'slice_sao_luma_flag': 'slice_sao_luma_flag',
        'slice_sao_chroma_flag': 'slice_sao_chroma_flag',
        'num_ref_idx_active_override_flag': 'num_ref_idx_active_override_flag',
        'mvd_l1_zero_flag': 'mvd_l1_zero_flag',
        'cabac_init_flag': 'cabac_init_flag',
        'cu_chroma_qp_offset_enabled_flag': 'cu_chroma_qp_offset_enabled_flag',
        'deblocking_filter_override_flag': 'deblocking_filter_override_flag',
        'slice_deblocking_filter_disabled_flag': 'slice_deblocking_filter_disabled_flag',
        'collocated_from_l0_flag': 'collocated_from_l0_flag',
        'slice_loop_filter_across_slices_enabled_flag': 'slice_loop_filter_across_slices_enabled_flag',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std_encode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoEncodeH265SliceSegmentHeaderFlags._type_ = {
    'first_slice_segment_in_pic_flag': ctypes.c_uint32,
    'dependent_slice_segment_flag': ctypes.c_uint32,
    'slice_sao_luma_flag': ctypes.c_uint32,
    'slice_sao_chroma_flag': ctypes.c_uint32,
    'num_ref_idx_active_override_flag': ctypes.c_uint32,
    'mvd_l1_zero_flag': ctypes.c_uint32,
    'cabac_init_flag': ctypes.c_uint32,
    'cu_chroma_qp_offset_enabled_flag': ctypes.c_uint32,
    'deblocking_filter_override_flag': ctypes.c_uint32,
    'slice_deblocking_filter_disabled_flag': ctypes.c_uint32,
    'collocated_from_l0_flag': ctypes.c_uint32,
    'slice_loop_filter_across_slices_enabled_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
