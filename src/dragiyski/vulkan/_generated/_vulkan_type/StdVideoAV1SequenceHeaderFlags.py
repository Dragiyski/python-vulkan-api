import ctypes

class StdVideoAV1SequenceHeaderFlags(ctypes.Structure):
    _fields_ = [
        ('still_picture', ctypes.c_uint32, 1),
        ('reduced_still_picture_header', ctypes.c_uint32, 1),
        ('use_128x128_superblock', ctypes.c_uint32, 1),
        ('enable_filter_intra', ctypes.c_uint32, 1),
        ('enable_intra_edge_filter', ctypes.c_uint32, 1),
        ('enable_interintra_compound', ctypes.c_uint32, 1),
        ('enable_masked_compound', ctypes.c_uint32, 1),
        ('enable_warped_motion', ctypes.c_uint32, 1),
        ('enable_dual_filter', ctypes.c_uint32, 1),
        ('enable_order_hint', ctypes.c_uint32, 1),
        ('enable_jnt_comp', ctypes.c_uint32, 1),
        ('enable_ref_frame_mvs', ctypes.c_uint32, 1),
        ('frame_id_numbers_present_flag', ctypes.c_uint32, 1),
        ('enable_superres', ctypes.c_uint32, 1),
        ('enable_cdef', ctypes.c_uint32, 1),
        ('enable_restoration', ctypes.c_uint32, 1),
        ('film_grain_params_present', ctypes.c_uint32, 1),
        ('timing_info_present_flag', ctypes.c_uint32, 1),
        ('initial_display_delay_present_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 13),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoAV1SequenceHeader',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'still_picture': 'still_picture',
        'reduced_still_picture_header': 'reduced_still_picture_header',
        'use_128x128_superblock': 'use_128x128_superblock',
        'enable_filter_intra': 'enable_filter_intra',
        'enable_intra_edge_filter': 'enable_intra_edge_filter',
        'enable_interintra_compound': 'enable_interintra_compound',
        'enable_masked_compound': 'enable_masked_compound',
        'enable_warped_motion': 'enable_warped_motion',
        'enable_dual_filter': 'enable_dual_filter',
        'enable_order_hint': 'enable_order_hint',
        'enable_jnt_comp': 'enable_jnt_comp',
        'enable_ref_frame_mvs': 'enable_ref_frame_mvs',
        'frame_id_numbers_present_flag': 'frame_id_numbers_present_flag',
        'enable_superres': 'enable_superres',
        'enable_cdef': 'enable_cdef',
        'enable_restoration': 'enable_restoration',
        'film_grain_params_present': 'film_grain_params_present',
        'timing_info_present_flag': 'timing_info_present_flag',
        'initial_display_delay_present_flag': 'initial_display_delay_present_flag',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoAV1SequenceHeaderFlags._type_ = {
    'still_picture': ctypes.c_uint32,
    'reduced_still_picture_header': ctypes.c_uint32,
    'use_128x128_superblock': ctypes.c_uint32,
    'enable_filter_intra': ctypes.c_uint32,
    'enable_intra_edge_filter': ctypes.c_uint32,
    'enable_interintra_compound': ctypes.c_uint32,
    'enable_masked_compound': ctypes.c_uint32,
    'enable_warped_motion': ctypes.c_uint32,
    'enable_dual_filter': ctypes.c_uint32,
    'enable_order_hint': ctypes.c_uint32,
    'enable_jnt_comp': ctypes.c_uint32,
    'enable_ref_frame_mvs': ctypes.c_uint32,
    'frame_id_numbers_present_flag': ctypes.c_uint32,
    'enable_superres': ctypes.c_uint32,
    'enable_cdef': ctypes.c_uint32,
    'enable_restoration': ctypes.c_uint32,
    'film_grain_params_present': ctypes.c_uint32,
    'timing_info_present_flag': ctypes.c_uint32,
    'initial_display_delay_present_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
