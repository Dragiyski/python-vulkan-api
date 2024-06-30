from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265PictureParameterSet'
_member_list_ = ['flags', 'pps_pic_parameter_set_id', 'pps_seq_parameter_set_id', 'sps_video_parameter_set_id', 'num_extra_slice_header_bits', 'num_ref_idx_l0_default_active_minus1', 'num_ref_idx_l1_default_active_minus1', 'init_qp_minus26', 'diff_cu_qp_delta_depth', 'pps_cb_qp_offset', 'pps_cr_qp_offset', 'pps_beta_offset_div2', 'pps_tc_offset_div2', 'log2_parallel_merge_level_minus2', 'log2_max_transform_skip_block_size_minus2', 'diff_cu_chroma_qp_offset_depth', 'chroma_qp_offset_list_len_minus1', 'cb_qp_offset_list', 'cr_qp_offset_list', 'log2_sao_offset_scale_luma', 'log2_sao_offset_scale_chroma', 'pps_act_y_qp_offset_plus5', 'pps_act_cb_qp_offset_plus5', 'pps_act_cr_qp_offset_plus3', 'pps_num_palette_predictor_initializers', 'luma_bit_depth_entry_minus8', 'chroma_bit_depth_entry_minus8', 'num_tile_columns_minus1', 'num_tile_rows_minus1', 'reserved1', 'reserved2', 'column_width_minus1', 'row_height_minus1', 'reserved3', 'pScalingLists', 'pPredictorPaletteEntries']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH265PpsFlags'),
        'type_name': 'StdVideoH265PpsFlags',
        'structure': 'StdVideoH265PpsFlags',
        'is_string': False,
    },
    'pps_pic_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pps_seq_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'sps_video_parameter_set_id': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_extra_slice_header_bits': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_ref_idx_l0_default_active_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_ref_idx_l1_default_active_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'init_qp_minus26': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'diff_cu_qp_delta_depth': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pps_cb_qp_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pps_cr_qp_offset': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pps_beta_offset_div2': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pps_tc_offset_div2': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'log2_parallel_merge_level_minus2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_max_transform_skip_block_size_minus2': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'diff_cu_chroma_qp_offset_depth': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'chroma_qp_offset_list_len_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'cb_qp_offset_list': {
        'type': CArrayType(CIntType('c_int8'), 6),
        'is_string': False,
    },
    'cr_qp_offset_list': {
        'type': CArrayType(CIntType('c_int8'), 6),
        'is_string': False,
    },
    'log2_sao_offset_scale_luma': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_sao_offset_scale_chroma': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pps_act_y_qp_offset_plus5': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pps_act_cb_qp_offset_plus5': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pps_act_cr_qp_offset_plus3': {
        'type': CIntType('c_int8'),
        'is_string': False,
    },
    'pps_num_palette_predictor_initializers': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'luma_bit_depth_entry_minus8': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'chroma_bit_depth_entry_minus8': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_tile_columns_minus1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_tile_rows_minus1': {
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
    'column_width_minus1': {
        'type': CArrayType(CIntType('c_uint16'), 19),
        'is_string': False,
    },
    'row_height_minus1': {
        'type': CArrayType(CIntType('c_uint16'), 21),
        'is_string': False,
    },
    'reserved3': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pScalingLists': {
        'type': CPointerType(CComplexType('StdVideoH265ScalingLists')),
        'type_name': 'StdVideoH265ScalingLists',
        'structure': 'StdVideoH265ScalingLists',
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
    'StdVideoH265PpsFlags',
    'StdVideoH265PredictorPaletteEntries',
    'StdVideoH265ScalingLists',
}
_included_in_ = {
    'VkVideoDecodeH265SessionParametersAddInfoKHR',
    'VkVideoEncodeH265SessionParametersAddInfoKHR',
}
_input_of_ = set()
_output_of_ = set()
