from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265SequenceParameterSet'
_member_list_ = ['flags', 'chroma_format_idc', 'pic_width_in_luma_samples', 'pic_height_in_luma_samples', 'sps_video_parameter_set_id', 'sps_max_sub_layers_minus1', 'sps_seq_parameter_set_id', 'bit_depth_luma_minus8', 'bit_depth_chroma_minus8', 'log2_max_pic_order_cnt_lsb_minus4', 'log2_min_luma_coding_block_size_minus3', 'log2_diff_max_min_luma_coding_block_size', 'log2_min_luma_transform_block_size_minus2', 'log2_diff_max_min_luma_transform_block_size', 'max_transform_hierarchy_depth_inter', 'max_transform_hierarchy_depth_intra', 'num_short_term_ref_pic_sets', 'num_long_term_ref_pics_sps', 'pcm_sample_bit_depth_luma_minus1', 'pcm_sample_bit_depth_chroma_minus1', 'log2_min_pcm_luma_coding_block_size_minus3', 'log2_diff_max_min_pcm_luma_coding_block_size', 'reserved1', 'reserved2', 'palette_max_size', 'delta_palette_max_predictor_size', 'motion_vector_resolution_control_idc', 'sps_num_palette_predictor_initializers_minus1', 'conf_win_left_offset', 'conf_win_right_offset', 'conf_win_top_offset', 'conf_win_bottom_offset', 'pProfileTierLevel', 'pDecPicBufMgr', 'pScalingLists', 'pShortTermRefPicSet', 'pLongTermRefPicsSps', 'pSequenceParameterSetVui', 'pPredictorPaletteEntries']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH265SpsFlags'),
        'type_name': 'StdVideoH265SpsFlags',
        'structure': 'StdVideoH265SpsFlags',
        'is_string': False,
    },
    'chroma_format_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265ChromaFormatIdc',
        'enum': 'StdVideoH265ChromaFormatIdc',
        'is_string': False,
    },
    'pic_width_in_luma_samples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pic_height_in_luma_samples': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'sps_video_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'sps_max_sub_layers_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'sps_seq_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'bit_depth_luma_minus8': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'bit_depth_chroma_minus8': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_max_pic_order_cnt_lsb_minus4': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_min_luma_coding_block_size_minus3': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_diff_max_min_luma_coding_block_size': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_min_luma_transform_block_size_minus2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_diff_max_min_luma_transform_block_size': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'max_transform_hierarchy_depth_inter': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'max_transform_hierarchy_depth_intra': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_short_term_ref_pic_sets': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_long_term_ref_pics_sps': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pcm_sample_bit_depth_luma_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pcm_sample_bit_depth_chroma_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_min_pcm_luma_coding_block_size_minus3': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_diff_max_min_pcm_luma_coding_block_size': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'palette_max_size': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'delta_palette_max_predictor_size': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'motion_vector_resolution_control_idc': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'sps_num_palette_predictor_initializers_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'conf_win_left_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'conf_win_right_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'conf_win_top_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'conf_win_bottom_offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pProfileTierLevel': {
        'type': CPointerType(CComplexType('StdVideoH265ProfileTierLevel')),
        'type_name': 'StdVideoH265ProfileTierLevel',
        'structure': 'StdVideoH265ProfileTierLevel',
        'is_string': False,
    },
    'pDecPicBufMgr': {
        'type': CPointerType(CComplexType('StdVideoH265DecPicBufMgr')),
        'type_name': 'StdVideoH265DecPicBufMgr',
        'structure': 'StdVideoH265DecPicBufMgr',
        'is_string': False,
    },
    'pScalingLists': {
        'type': CPointerType(CComplexType('StdVideoH265ScalingLists')),
        'type_name': 'StdVideoH265ScalingLists',
        'structure': 'StdVideoH265ScalingLists',
        'is_string': False,
    },
    'pShortTermRefPicSet': {
        'type': CPointerType(CComplexType('StdVideoH265ShortTermRefPicSet')),
        'type_name': 'StdVideoH265ShortTermRefPicSet',
        'structure': 'StdVideoH265ShortTermRefPicSet',
        'is_string': False,
    },
    'pLongTermRefPicsSps': {
        'type': CPointerType(CComplexType('StdVideoH265LongTermRefPicsSps')),
        'type_name': 'StdVideoH265LongTermRefPicsSps',
        'structure': 'StdVideoH265LongTermRefPicsSps',
        'is_string': False,
    },
    'pSequenceParameterSetVui': {
        'type': CPointerType(CComplexType('StdVideoH265SequenceParameterSetVui')),
        'type_name': 'StdVideoH265SequenceParameterSetVui',
        'structure': 'StdVideoH265SequenceParameterSetVui',
        'is_string': False,
    },
    'pPredictorPaletteEntries': {
        'type': CPointerType(CComplexType('StdVideoH265PredictorPaletteEntries')),
        'type_name': 'StdVideoH265PredictorPaletteEntries',
        'structure': 'StdVideoH265PredictorPaletteEntries',
        'is_string': False,
    },
}
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
