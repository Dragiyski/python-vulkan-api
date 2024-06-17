import ctypes, sys

class StdVideoH265PpsFlags(ctypes.Structure):
    _fields_ = [
        ('dependent_slice_segments_enabled_flag', ctypes.c_uint32, 1),
        ('output_flag_present_flag', ctypes.c_uint32, 1),
        ('sign_data_hiding_enabled_flag', ctypes.c_uint32, 1),
        ('cabac_init_present_flag', ctypes.c_uint32, 1),
        ('constrained_intra_pred_flag', ctypes.c_uint32, 1),
        ('transform_skip_enabled_flag', ctypes.c_uint32, 1),
        ('cu_qp_delta_enabled_flag', ctypes.c_uint32, 1),
        ('pps_slice_chroma_qp_offsets_present_flag', ctypes.c_uint32, 1),
        ('weighted_pred_flag', ctypes.c_uint32, 1),
        ('weighted_bipred_flag', ctypes.c_uint32, 1),
        ('transquant_bypass_enabled_flag', ctypes.c_uint32, 1),
        ('tiles_enabled_flag', ctypes.c_uint32, 1),
        ('entropy_coding_sync_enabled_flag', ctypes.c_uint32, 1),
        ('uniform_spacing_flag', ctypes.c_uint32, 1),
        ('loop_filter_across_tiles_enabled_flag', ctypes.c_uint32, 1),
        ('pps_loop_filter_across_slices_enabled_flag', ctypes.c_uint32, 1),
        ('deblocking_filter_control_present_flag', ctypes.c_uint32, 1),
        ('deblocking_filter_override_enabled_flag', ctypes.c_uint32, 1),
        ('pps_deblocking_filter_disabled_flag', ctypes.c_uint32, 1),
        ('pps_scaling_list_data_present_flag', ctypes.c_uint32, 1),
        ('lists_modification_present_flag', ctypes.c_uint32, 1),
        ('slice_segment_header_extension_present_flag', ctypes.c_uint32, 1),
        ('pps_extension_present_flag', ctypes.c_uint32, 1),
        ('cross_component_prediction_enabled_flag', ctypes.c_uint32, 1),
        ('chroma_qp_offset_list_enabled_flag', ctypes.c_uint32, 1),
        ('pps_curr_pic_ref_enabled_flag', ctypes.c_uint32, 1),
        ('residual_adaptive_colour_transform_enabled_flag', ctypes.c_uint32, 1),
        ('pps_slice_act_qp_offsets_present_flag', ctypes.c_uint32, 1),
        ('pps_palette_predictor_initializers_present_flag', ctypes.c_uint32, 1),
        ('monochrome_palette_flag', ctypes.c_uint32, 1),
        ('pps_range_extension_flag', ctypes.c_uint32, 1),
    ]

sys.modules[__name__] = StdVideoH265PpsFlags
