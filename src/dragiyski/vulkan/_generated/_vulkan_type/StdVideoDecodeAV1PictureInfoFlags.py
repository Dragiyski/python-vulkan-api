import ctypes

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

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoDecodeAV1PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'error_resilient_mode': 'error_resilient_mode',
        'disable_cdf_update': 'disable_cdf_update',
        'use_superres': 'use_superres',
        'render_and_frame_size_different': 'render_and_frame_size_different',
        'allow_screen_content_tools': 'allow_screen_content_tools',
        'is_filter_switchable': 'is_filter_switchable',
        'force_integer_mv': 'force_integer_mv',
        'frame_size_override_flag': 'frame_size_override_flag',
        'buffer_removal_time_present_flag': 'buffer_removal_time_present_flag',
        'allow_intrabc': 'allow_intrabc',
        'frame_refs_short_signaling': 'frame_refs_short_signaling',
        'allow_high_precision_mv': 'allow_high_precision_mv',
        'is_motion_mode_switchable': 'is_motion_mode_switchable',
        'use_ref_frame_mvs': 'use_ref_frame_mvs',
        'disable_frame_end_update_cdf': 'disable_frame_end_update_cdf',
        'allow_warped_motion': 'allow_warped_motion',
        'reduced_tx_set': 'reduced_tx_set',
        'reference_select': 'reference_select',
        'skip_mode_present': 'skip_mode_present',
        'delta_q_present': 'delta_q_present',
        'delta_lf_present': 'delta_lf_present',
        'delta_lf_multi': 'delta_lf_multi',
        'segmentation_enabled': 'segmentation_enabled',
        'segmentation_update_map': 'segmentation_update_map',
        'segmentation_temporal_update': 'segmentation_temporal_update',
        'segmentation_update_data': 'segmentation_update_data',
        'UsesLr': 'uses_lr',
        'usesChromaLr': 'uses_chroma_lr',
        'apply_grain': 'apply_grain',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std_decode',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoDecodeAV1PictureInfoFlags._type_ = {
    'error_resilient_mode': ctypes.c_uint32,
    'disable_cdf_update': ctypes.c_uint32,
    'use_superres': ctypes.c_uint32,
    'render_and_frame_size_different': ctypes.c_uint32,
    'allow_screen_content_tools': ctypes.c_uint32,
    'is_filter_switchable': ctypes.c_uint32,
    'force_integer_mv': ctypes.c_uint32,
    'frame_size_override_flag': ctypes.c_uint32,
    'buffer_removal_time_present_flag': ctypes.c_uint32,
    'allow_intrabc': ctypes.c_uint32,
    'frame_refs_short_signaling': ctypes.c_uint32,
    'allow_high_precision_mv': ctypes.c_uint32,
    'is_motion_mode_switchable': ctypes.c_uint32,
    'use_ref_frame_mvs': ctypes.c_uint32,
    'disable_frame_end_update_cdf': ctypes.c_uint32,
    'allow_warped_motion': ctypes.c_uint32,
    'reduced_tx_set': ctypes.c_uint32,
    'reference_select': ctypes.c_uint32,
    'skip_mode_present': ctypes.c_uint32,
    'delta_q_present': ctypes.c_uint32,
    'delta_lf_present': ctypes.c_uint32,
    'delta_lf_multi': ctypes.c_uint32,
    'segmentation_enabled': ctypes.c_uint32,
    'segmentation_update_map': ctypes.c_uint32,
    'segmentation_temporal_update': ctypes.c_uint32,
    'segmentation_update_data': ctypes.c_uint32,
    'UsesLr': ctypes.c_uint32,
    'usesChromaLr': ctypes.c_uint32,
    'apply_grain': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
