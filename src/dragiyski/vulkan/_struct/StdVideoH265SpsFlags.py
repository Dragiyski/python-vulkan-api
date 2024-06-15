import ctypes, sys

class StdVideoH265SpsFlags(ctypes.Structure):
    _fields_ = [
        ('sps_temporal_id_nesting_flag', ctypes.c_uint32, 1),
        ('separate_colour_plane_flag', ctypes.c_uint32, 1),
        ('conformance_window_flag', ctypes.c_uint32, 1),
        ('sps_sub_layer_ordering_info_present_flag', ctypes.c_uint32, 1),
        ('scaling_list_enabled_flag', ctypes.c_uint32, 1),
        ('sps_scaling_list_data_present_flag', ctypes.c_uint32, 1),
        ('amp_enabled_flag', ctypes.c_uint32, 1),
        ('sample_adaptive_offset_enabled_flag', ctypes.c_uint32, 1),
        ('pcm_enabled_flag', ctypes.c_uint32, 1),
        ('pcm_loop_filter_disabled_flag', ctypes.c_uint32, 1),
        ('long_term_ref_pics_present_flag', ctypes.c_uint32, 1),
        ('sps_temporal_mvp_enabled_flag', ctypes.c_uint32, 1),
        ('strong_intra_smoothing_enabled_flag', ctypes.c_uint32, 1),
        ('vui_parameters_present_flag', ctypes.c_uint32, 1),
        ('sps_extension_present_flag', ctypes.c_uint32, 1),
        ('sps_range_extension_flag', ctypes.c_uint32, 1),
        ('transform_skip_rotation_enabled_flag', ctypes.c_uint32, 1),
        ('transform_skip_context_enabled_flag', ctypes.c_uint32, 1),
        ('implicit_rdpcm_enabled_flag', ctypes.c_uint32, 1),
        ('explicit_rdpcm_enabled_flag', ctypes.c_uint32, 1),
        ('extended_precision_processing_flag', ctypes.c_uint32, 1),
        ('intra_smoothing_disabled_flag', ctypes.c_uint32, 1),
        ('high_precision_offsets_enabled_flag', ctypes.c_uint32, 1),
        ('persistent_rice_adaptation_enabled_flag', ctypes.c_uint32, 1),
        ('cabac_bypass_alignment_enabled_flag', ctypes.c_uint32, 1),
        ('sps_scc_extension_flag', ctypes.c_uint32, 1),
        ('sps_curr_pic_ref_enabled_flag', ctypes.c_uint32, 1),
        ('palette_mode_enabled_flag', ctypes.c_uint32, 1),
        ('sps_palette_predictor_initializers_present_flag', ctypes.c_uint32, 1),
        ('intra_boundary_filtering_disabled_flag', ctypes.c_uint32, 1),
    ]

sys.modules[__name__] = StdVideoH265SpsFlags
