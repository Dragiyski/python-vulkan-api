import ctypes

class StdVideoH265SequenceParameterSet(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH265DecPicBufMgr',
        'StdVideoH265LongTermRefPicsSps',
        'StdVideoH265PredictorPaletteEntries',
        'StdVideoH265ProfileTierLevel',
        'StdVideoH265ScalingLists',
        'StdVideoH265SequenceParameterSetVui',
        'StdVideoH265ShortTermRefPicSet',
        'StdVideoH265SpsFlags',
    }
    _included_in_ = {
        'VkVideoDecodeH265SessionParametersAddInfoKHR',
        'VkVideoEncodeH265SessionParametersAddInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'chroma_format_idc': 'chroma_format_idc',
        'pic_width_in_luma_samples': 'pic_width_in_luma_samples',
        'pic_height_in_luma_samples': 'pic_height_in_luma_samples',
        'sps_video_parameter_set_id': 'sps_video_parameter_set_id',
        'sps_max_sub_layers_minus1': 'sps_max_sub_layers_minus1',
        'sps_seq_parameter_set_id': 'sps_seq_parameter_set_id',
        'bit_depth_luma_minus8': 'bit_depth_luma_minus8',
        'bit_depth_chroma_minus8': 'bit_depth_chroma_minus8',
        'log2_max_pic_order_cnt_lsb_minus4': 'log2_max_pic_order_cnt_lsb_minus4',
        'log2_min_luma_coding_block_size_minus3': 'log2_min_luma_coding_block_size_minus3',
        'log2_diff_max_min_luma_coding_block_size': 'log2_diff_max_min_luma_coding_block_size',
        'log2_min_luma_transform_block_size_minus2': 'log2_min_luma_transform_block_size_minus2',
        'log2_diff_max_min_luma_transform_block_size': 'log2_diff_max_min_luma_transform_block_size',
        'max_transform_hierarchy_depth_inter': 'max_transform_hierarchy_depth_inter',
        'max_transform_hierarchy_depth_intra': 'max_transform_hierarchy_depth_intra',
        'num_short_term_ref_pic_sets': 'num_short_term_ref_pic_sets',
        'num_long_term_ref_pics_sps': 'num_long_term_ref_pics_sps',
        'pcm_sample_bit_depth_luma_minus1': 'pcm_sample_bit_depth_luma_minus1',
        'pcm_sample_bit_depth_chroma_minus1': 'pcm_sample_bit_depth_chroma_minus1',
        'log2_min_pcm_luma_coding_block_size_minus3': 'log2_min_pcm_luma_coding_block_size_minus3',
        'log2_diff_max_min_pcm_luma_coding_block_size': 'log2_diff_max_min_pcm_luma_coding_block_size',
        'reserved1': 'reserved1',
        'reserved2': 'reserved2',
        'palette_max_size': 'palette_max_size',
        'delta_palette_max_predictor_size': 'delta_palette_max_predictor_size',
        'motion_vector_resolution_control_idc': 'motion_vector_resolution_control_idc',
        'sps_num_palette_predictor_initializers_minus1': 'sps_num_palette_predictor_initializers_minus1',
        'conf_win_left_offset': 'conf_win_left_offset',
        'conf_win_right_offset': 'conf_win_right_offset',
        'conf_win_top_offset': 'conf_win_top_offset',
        'conf_win_bottom_offset': 'conf_win_bottom_offset',
        'pProfileTierLevel': 'profile_tier_level',
        'pDecPicBufMgr': 'dec_pic_buf_mgr',
        'pScalingLists': 'scaling_lists',
        'pShortTermRefPicSet': 'short_term_ref_pic_set',
        'pLongTermRefPicsSps': 'long_term_ref_pics_sps',
        'pSequenceParameterSetVui': 'sequence_parameter_set_vui',
        'pPredictorPaletteEntries': 'predictor_palette_entries',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_h265std',
    }
    _vk_enum_ = {
        'chroma_format_idc': 'StdVideoH265ChromaFormatIdc',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoH265DecPicBufMgr import StdVideoH265DecPicBufMgr
from .StdVideoH265LongTermRefPicsSps import StdVideoH265LongTermRefPicsSps
from .StdVideoH265PredictorPaletteEntries import StdVideoH265PredictorPaletteEntries
from .StdVideoH265ProfileTierLevel import StdVideoH265ProfileTierLevel
from .StdVideoH265ScalingLists import StdVideoH265ScalingLists
from .StdVideoH265SequenceParameterSetVui import StdVideoH265SequenceParameterSetVui
from .StdVideoH265ShortTermRefPicSet import StdVideoH265ShortTermRefPicSet
from .StdVideoH265SpsFlags import StdVideoH265SpsFlags

StdVideoH265SequenceParameterSet._fields_ = [
    ('flags', StdVideoH265SpsFlags),
    ('chroma_format_idc', ctypes.c_int),
    ('pic_width_in_luma_samples', ctypes.c_uint32),
    ('pic_height_in_luma_samples', ctypes.c_uint32),
    ('sps_video_parameter_set_id', ctypes.c_uint8),
    ('sps_max_sub_layers_minus1', ctypes.c_uint8),
    ('sps_seq_parameter_set_id', ctypes.c_uint8),
    ('bit_depth_luma_minus8', ctypes.c_uint8),
    ('bit_depth_chroma_minus8', ctypes.c_uint8),
    ('log2_max_pic_order_cnt_lsb_minus4', ctypes.c_uint8),
    ('log2_min_luma_coding_block_size_minus3', ctypes.c_uint8),
    ('log2_diff_max_min_luma_coding_block_size', ctypes.c_uint8),
    ('log2_min_luma_transform_block_size_minus2', ctypes.c_uint8),
    ('log2_diff_max_min_luma_transform_block_size', ctypes.c_uint8),
    ('max_transform_hierarchy_depth_inter', ctypes.c_uint8),
    ('max_transform_hierarchy_depth_intra', ctypes.c_uint8),
    ('num_short_term_ref_pic_sets', ctypes.c_uint8),
    ('num_long_term_ref_pics_sps', ctypes.c_uint8),
    ('pcm_sample_bit_depth_luma_minus1', ctypes.c_uint8),
    ('pcm_sample_bit_depth_chroma_minus1', ctypes.c_uint8),
    ('log2_min_pcm_luma_coding_block_size_minus3', ctypes.c_uint8),
    ('log2_diff_max_min_pcm_luma_coding_block_size', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('reserved2', ctypes.c_uint8),
    ('palette_max_size', ctypes.c_uint8),
    ('delta_palette_max_predictor_size', ctypes.c_uint8),
    ('motion_vector_resolution_control_idc', ctypes.c_uint8),
    ('sps_num_palette_predictor_initializers_minus1', ctypes.c_uint8),
    ('conf_win_left_offset', ctypes.c_uint32),
    ('conf_win_right_offset', ctypes.c_uint32),
    ('conf_win_top_offset', ctypes.c_uint32),
    ('conf_win_bottom_offset', ctypes.c_uint32),
    ('pProfileTierLevel', ctypes.POINTER(StdVideoH265ProfileTierLevel)),
    ('pDecPicBufMgr', ctypes.POINTER(StdVideoH265DecPicBufMgr)),
    ('pScalingLists', ctypes.POINTER(StdVideoH265ScalingLists)),
    ('pShortTermRefPicSet', ctypes.POINTER(StdVideoH265ShortTermRefPicSet)),
    ('pLongTermRefPicsSps', ctypes.POINTER(StdVideoH265LongTermRefPicsSps)),
    ('pSequenceParameterSetVui', ctypes.POINTER(StdVideoH265SequenceParameterSetVui)),
    ('pPredictorPaletteEntries', ctypes.POINTER(StdVideoH265PredictorPaletteEntries)),
]

StdVideoH265SequenceParameterSet._type_ = {
    'flags': StdVideoH265SpsFlags,
    'chroma_format_idc': ctypes.c_int,
    'pic_width_in_luma_samples': ctypes.c_uint32,
    'pic_height_in_luma_samples': ctypes.c_uint32,
    'sps_video_parameter_set_id': ctypes.c_uint8,
    'sps_max_sub_layers_minus1': ctypes.c_uint8,
    'sps_seq_parameter_set_id': ctypes.c_uint8,
    'bit_depth_luma_minus8': ctypes.c_uint8,
    'bit_depth_chroma_minus8': ctypes.c_uint8,
    'log2_max_pic_order_cnt_lsb_minus4': ctypes.c_uint8,
    'log2_min_luma_coding_block_size_minus3': ctypes.c_uint8,
    'log2_diff_max_min_luma_coding_block_size': ctypes.c_uint8,
    'log2_min_luma_transform_block_size_minus2': ctypes.c_uint8,
    'log2_diff_max_min_luma_transform_block_size': ctypes.c_uint8,
    'max_transform_hierarchy_depth_inter': ctypes.c_uint8,
    'max_transform_hierarchy_depth_intra': ctypes.c_uint8,
    'num_short_term_ref_pic_sets': ctypes.c_uint8,
    'num_long_term_ref_pics_sps': ctypes.c_uint8,
    'pcm_sample_bit_depth_luma_minus1': ctypes.c_uint8,
    'pcm_sample_bit_depth_chroma_minus1': ctypes.c_uint8,
    'log2_min_pcm_luma_coding_block_size_minus3': ctypes.c_uint8,
    'log2_diff_max_min_pcm_luma_coding_block_size': ctypes.c_uint8,
    'reserved1': ctypes.c_uint8,
    'reserved2': ctypes.c_uint8,
    'palette_max_size': ctypes.c_uint8,
    'delta_palette_max_predictor_size': ctypes.c_uint8,
    'motion_vector_resolution_control_idc': ctypes.c_uint8,
    'sps_num_palette_predictor_initializers_minus1': ctypes.c_uint8,
    'conf_win_left_offset': ctypes.c_uint32,
    'conf_win_right_offset': ctypes.c_uint32,
    'conf_win_top_offset': ctypes.c_uint32,
    'conf_win_bottom_offset': ctypes.c_uint32,
    'pProfileTierLevel': ctypes.POINTER(StdVideoH265ProfileTierLevel),
    'pDecPicBufMgr': ctypes.POINTER(StdVideoH265DecPicBufMgr),
    'pScalingLists': ctypes.POINTER(StdVideoH265ScalingLists),
    'pShortTermRefPicSet': ctypes.POINTER(StdVideoH265ShortTermRefPicSet),
    'pLongTermRefPicsSps': ctypes.POINTER(StdVideoH265LongTermRefPicsSps),
    'pSequenceParameterSetVui': ctypes.POINTER(StdVideoH265SequenceParameterSetVui),
    'pPredictorPaletteEntries': ctypes.POINTER(StdVideoH265PredictorPaletteEntries),
}
