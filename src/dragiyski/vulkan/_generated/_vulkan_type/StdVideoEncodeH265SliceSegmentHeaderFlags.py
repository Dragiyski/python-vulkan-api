import ctypes, sys

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

sys.modules[__name__] = StdVideoEncodeH265SliceSegmentHeaderFlags
