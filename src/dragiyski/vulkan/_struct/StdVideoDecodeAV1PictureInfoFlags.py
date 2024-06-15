import ctypes, sys

class StdVideoDecodeAV1PictureInfoFlags(ctypes.Structure):
    _fields_ = [
        ('error_resilient_mode', ctypes.c_uint32, 1),
        ('disable_cdf_update', ctypes.c_uint32, 1),
        ('use_superres', ctypes.c_uint32, 1),
        ('render_and_frame_size_different', ctypes.c_uint32, 1),
        ('allow_screen_content_tools', ctypes.c_uint32, 1),
        ('is_filter_switchable', ctypes.c_uint32, 1),
        ('force_integer_mv', ctypes.c_uint32, 1),
        ('frame_size_override_flag', ctypes.c_uint32, 1),
        ('buffer_removal_time_present_flag', ctypes.c_uint32, 1),
        ('allow_intrabc', ctypes.c_uint32, 1),
        ('frame_refs_short_signaling', ctypes.c_uint32, 1),
        ('allow_high_precision_mv', ctypes.c_uint32, 1),
        ('is_motion_mode_switchable', ctypes.c_uint32, 1),
        ('use_ref_frame_mvs', ctypes.c_uint32, 1),
        ('disable_frame_end_update_cdf', ctypes.c_uint32, 1),
        ('allow_warped_motion', ctypes.c_uint32, 1),
        ('reduced_tx_set', ctypes.c_uint32, 1),
        ('reference_select', ctypes.c_uint32, 1),
        ('skip_mode_present', ctypes.c_uint32, 1),
        ('delta_q_present', ctypes.c_uint32, 1),
        ('delta_lf_present', ctypes.c_uint32, 1),
        ('delta_lf_multi', ctypes.c_uint32, 1),
        ('segmentation_enabled', ctypes.c_uint32, 1),
        ('segmentation_update_map', ctypes.c_uint32, 1),
        ('segmentation_temporal_update', ctypes.c_uint32, 1),
        ('segmentation_update_data', ctypes.c_uint32, 1),
        ('UsesLr', ctypes.c_uint32, 1),
        ('usesChromaLr', ctypes.c_uint32, 1),
        ('apply_grain', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 3),
    ]

sys.modules[__name__] = StdVideoDecodeAV1PictureInfoFlags
