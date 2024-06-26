import ctypes

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

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265SequenceParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sps_temporal_id_nesting_flag': 'sps_temporal_id_nesting_flag',
        'separate_colour_plane_flag': 'separate_colour_plane_flag',
        'conformance_window_flag': 'conformance_window_flag',
        'sps_sub_layer_ordering_info_present_flag': 'sps_sub_layer_ordering_info_present_flag',
        'scaling_list_enabled_flag': 'scaling_list_enabled_flag',
        'sps_scaling_list_data_present_flag': 'sps_scaling_list_data_present_flag',
        'amp_enabled_flag': 'amp_enabled_flag',
        'sample_adaptive_offset_enabled_flag': 'sample_adaptive_offset_enabled_flag',
        'pcm_enabled_flag': 'pcm_enabled_flag',
        'pcm_loop_filter_disabled_flag': 'pcm_loop_filter_disabled_flag',
        'long_term_ref_pics_present_flag': 'long_term_ref_pics_present_flag',
        'sps_temporal_mvp_enabled_flag': 'sps_temporal_mvp_enabled_flag',
        'strong_intra_smoothing_enabled_flag': 'strong_intra_smoothing_enabled_flag',
        'vui_parameters_present_flag': 'vui_parameters_present_flag',
        'sps_extension_present_flag': 'sps_extension_present_flag',
        'sps_range_extension_flag': 'sps_range_extension_flag',
        'transform_skip_rotation_enabled_flag': 'transform_skip_rotation_enabled_flag',
        'transform_skip_context_enabled_flag': 'transform_skip_context_enabled_flag',
        'implicit_rdpcm_enabled_flag': 'implicit_rdpcm_enabled_flag',
        'explicit_rdpcm_enabled_flag': 'explicit_rdpcm_enabled_flag',
        'extended_precision_processing_flag': 'extended_precision_processing_flag',
        'intra_smoothing_disabled_flag': 'intra_smoothing_disabled_flag',
        'high_precision_offsets_enabled_flag': 'high_precision_offsets_enabled_flag',
        'persistent_rice_adaptation_enabled_flag': 'persistent_rice_adaptation_enabled_flag',
        'cabac_bypass_alignment_enabled_flag': 'cabac_bypass_alignment_enabled_flag',
        'sps_scc_extension_flag': 'sps_scc_extension_flag',
        'sps_curr_pic_ref_enabled_flag': 'sps_curr_pic_ref_enabled_flag',
        'palette_mode_enabled_flag': 'palette_mode_enabled_flag',
        'sps_palette_predictor_initializers_present_flag': 'sps_palette_predictor_initializers_present_flag',
        'intra_boundary_filtering_disabled_flag': 'intra_boundary_filtering_disabled_flag',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoH265SpsFlags._type_ = {
    'sps_temporal_id_nesting_flag': ctypes.c_uint32,
    'separate_colour_plane_flag': ctypes.c_uint32,
    'conformance_window_flag': ctypes.c_uint32,
    'sps_sub_layer_ordering_info_present_flag': ctypes.c_uint32,
    'scaling_list_enabled_flag': ctypes.c_uint32,
    'sps_scaling_list_data_present_flag': ctypes.c_uint32,
    'amp_enabled_flag': ctypes.c_uint32,
    'sample_adaptive_offset_enabled_flag': ctypes.c_uint32,
    'pcm_enabled_flag': ctypes.c_uint32,
    'pcm_loop_filter_disabled_flag': ctypes.c_uint32,
    'long_term_ref_pics_present_flag': ctypes.c_uint32,
    'sps_temporal_mvp_enabled_flag': ctypes.c_uint32,
    'strong_intra_smoothing_enabled_flag': ctypes.c_uint32,
    'vui_parameters_present_flag': ctypes.c_uint32,
    'sps_extension_present_flag': ctypes.c_uint32,
    'sps_range_extension_flag': ctypes.c_uint32,
    'transform_skip_rotation_enabled_flag': ctypes.c_uint32,
    'transform_skip_context_enabled_flag': ctypes.c_uint32,
    'implicit_rdpcm_enabled_flag': ctypes.c_uint32,
    'explicit_rdpcm_enabled_flag': ctypes.c_uint32,
    'extended_precision_processing_flag': ctypes.c_uint32,
    'intra_smoothing_disabled_flag': ctypes.c_uint32,
    'high_precision_offsets_enabled_flag': ctypes.c_uint32,
    'persistent_rice_adaptation_enabled_flag': ctypes.c_uint32,
    'cabac_bypass_alignment_enabled_flag': ctypes.c_uint32,
    'sps_scc_extension_flag': ctypes.c_uint32,
    'sps_curr_pic_ref_enabled_flag': ctypes.c_uint32,
    'palette_mode_enabled_flag': ctypes.c_uint32,
    'sps_palette_predictor_initializers_present_flag': ctypes.c_uint32,
    'intra_boundary_filtering_disabled_flag': ctypes.c_uint32,
}
