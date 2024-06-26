import ctypes

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

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoH265PictureParameterSet',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'dependent_slice_segments_enabled_flag': 'dependent_slice_segments_enabled_flag',
        'output_flag_present_flag': 'output_flag_present_flag',
        'sign_data_hiding_enabled_flag': 'sign_data_hiding_enabled_flag',
        'cabac_init_present_flag': 'cabac_init_present_flag',
        'constrained_intra_pred_flag': 'constrained_intra_pred_flag',
        'transform_skip_enabled_flag': 'transform_skip_enabled_flag',
        'cu_qp_delta_enabled_flag': 'cu_qp_delta_enabled_flag',
        'pps_slice_chroma_qp_offsets_present_flag': 'pps_slice_chroma_qp_offsets_present_flag',
        'weighted_pred_flag': 'weighted_pred_flag',
        'weighted_bipred_flag': 'weighted_bipred_flag',
        'transquant_bypass_enabled_flag': 'transquant_bypass_enabled_flag',
        'tiles_enabled_flag': 'tiles_enabled_flag',
        'entropy_coding_sync_enabled_flag': 'entropy_coding_sync_enabled_flag',
        'uniform_spacing_flag': 'uniform_spacing_flag',
        'loop_filter_across_tiles_enabled_flag': 'loop_filter_across_tiles_enabled_flag',
        'pps_loop_filter_across_slices_enabled_flag': 'pps_loop_filter_across_slices_enabled_flag',
        'deblocking_filter_control_present_flag': 'deblocking_filter_control_present_flag',
        'deblocking_filter_override_enabled_flag': 'deblocking_filter_override_enabled_flag',
        'pps_deblocking_filter_disabled_flag': 'pps_deblocking_filter_disabled_flag',
        'pps_scaling_list_data_present_flag': 'pps_scaling_list_data_present_flag',
        'lists_modification_present_flag': 'lists_modification_present_flag',
        'slice_segment_header_extension_present_flag': 'slice_segment_header_extension_present_flag',
        'pps_extension_present_flag': 'pps_extension_present_flag',
        'cross_component_prediction_enabled_flag': 'cross_component_prediction_enabled_flag',
        'chroma_qp_offset_list_enabled_flag': 'chroma_qp_offset_list_enabled_flag',
        'pps_curr_pic_ref_enabled_flag': 'pps_curr_pic_ref_enabled_flag',
        'residual_adaptive_colour_transform_enabled_flag': 'residual_adaptive_colour_transform_enabled_flag',
        'pps_slice_act_qp_offsets_present_flag': 'pps_slice_act_qp_offsets_present_flag',
        'pps_palette_predictor_initializers_present_flag': 'pps_palette_predictor_initializers_present_flag',
        'monochrome_palette_flag': 'monochrome_palette_flag',
        'pps_range_extension_flag': 'pps_range_extension_flag',
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

StdVideoH265PpsFlags._type_ = {
    'dependent_slice_segments_enabled_flag': ctypes.c_uint32,
    'output_flag_present_flag': ctypes.c_uint32,
    'sign_data_hiding_enabled_flag': ctypes.c_uint32,
    'cabac_init_present_flag': ctypes.c_uint32,
    'constrained_intra_pred_flag': ctypes.c_uint32,
    'transform_skip_enabled_flag': ctypes.c_uint32,
    'cu_qp_delta_enabled_flag': ctypes.c_uint32,
    'pps_slice_chroma_qp_offsets_present_flag': ctypes.c_uint32,
    'weighted_pred_flag': ctypes.c_uint32,
    'weighted_bipred_flag': ctypes.c_uint32,
    'transquant_bypass_enabled_flag': ctypes.c_uint32,
    'tiles_enabled_flag': ctypes.c_uint32,
    'entropy_coding_sync_enabled_flag': ctypes.c_uint32,
    'uniform_spacing_flag': ctypes.c_uint32,
    'loop_filter_across_tiles_enabled_flag': ctypes.c_uint32,
    'pps_loop_filter_across_slices_enabled_flag': ctypes.c_uint32,
    'deblocking_filter_control_present_flag': ctypes.c_uint32,
    'deblocking_filter_override_enabled_flag': ctypes.c_uint32,
    'pps_deblocking_filter_disabled_flag': ctypes.c_uint32,
    'pps_scaling_list_data_present_flag': ctypes.c_uint32,
    'lists_modification_present_flag': ctypes.c_uint32,
    'slice_segment_header_extension_present_flag': ctypes.c_uint32,
    'pps_extension_present_flag': ctypes.c_uint32,
    'cross_component_prediction_enabled_flag': ctypes.c_uint32,
    'chroma_qp_offset_list_enabled_flag': ctypes.c_uint32,
    'pps_curr_pic_ref_enabled_flag': ctypes.c_uint32,
    'residual_adaptive_colour_transform_enabled_flag': ctypes.c_uint32,
    'pps_slice_act_qp_offsets_present_flag': ctypes.c_uint32,
    'pps_palette_predictor_initializers_present_flag': ctypes.c_uint32,
    'monochrome_palette_flag': ctypes.c_uint32,
    'pps_range_extension_flag': ctypes.c_uint32,
}
