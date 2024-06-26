import ctypes

class StdVideoH265PictureParameterSet(ctypes.Structure):
    _init_ = []
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
    _python_name_ = {
        'flags': 'flags',
        'pps_pic_parameter_set_id': 'pps_pic_parameter_set_id',
        'pps_seq_parameter_set_id': 'pps_seq_parameter_set_id',
        'sps_video_parameter_set_id': 'sps_video_parameter_set_id',
        'num_extra_slice_header_bits': 'num_extra_slice_header_bits',
        'num_ref_idx_l0_default_active_minus1': 'num_ref_idx_l0_default_active_minus1',
        'num_ref_idx_l1_default_active_minus1': 'num_ref_idx_l1_default_active_minus1',
        'init_qp_minus26': 'init_qp_minus26',
        'diff_cu_qp_delta_depth': 'diff_cu_qp_delta_depth',
        'pps_cb_qp_offset': 'pps_cb_qp_offset',
        'pps_cr_qp_offset': 'pps_cr_qp_offset',
        'pps_beta_offset_div2': 'pps_beta_offset_div2',
        'pps_tc_offset_div2': 'pps_tc_offset_div2',
        'log2_parallel_merge_level_minus2': 'log2_parallel_merge_level_minus2',
        'log2_max_transform_skip_block_size_minus2': 'log2_max_transform_skip_block_size_minus2',
        'diff_cu_chroma_qp_offset_depth': 'diff_cu_chroma_qp_offset_depth',
        'chroma_qp_offset_list_len_minus1': 'chroma_qp_offset_list_len_minus1',
        'cb_qp_offset_list': 'cb_qp_offset_list',
        'cr_qp_offset_list': 'cr_qp_offset_list',
        'log2_sao_offset_scale_luma': 'log2_sao_offset_scale_luma',
        'log2_sao_offset_scale_chroma': 'log2_sao_offset_scale_chroma',
        'pps_act_y_qp_offset_plus5': 'pps_act_y_qp_offset_plus5',
        'pps_act_cb_qp_offset_plus5': 'pps_act_cb_qp_offset_plus5',
        'pps_act_cr_qp_offset_plus3': 'pps_act_cr_qp_offset_plus3',
        'pps_num_palette_predictor_initializers': 'pps_num_palette_predictor_initializers',
        'luma_bit_depth_entry_minus8': 'luma_bit_depth_entry_minus8',
        'chroma_bit_depth_entry_minus8': 'chroma_bit_depth_entry_minus8',
        'num_tile_columns_minus1': 'num_tile_columns_minus1',
        'num_tile_rows_minus1': 'num_tile_rows_minus1',
        'reserved1': 'reserved1',
        'reserved2': 'reserved2',
        'column_width_minus1': 'column_width_minus1',
        'row_height_minus1': 'row_height_minus1',
        'reserved3': 'reserved3',
        'pScalingLists': 'scaling_lists',
        'pPredictorPaletteEntries': 'predictor_palette_entries',
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


from .StdVideoH265PpsFlags import StdVideoH265PpsFlags
from .StdVideoH265PredictorPaletteEntries import StdVideoH265PredictorPaletteEntries
from .StdVideoH265ScalingLists import StdVideoH265ScalingLists

StdVideoH265PictureParameterSet._fields_ = [
    ('flags', StdVideoH265PpsFlags),
    ('pps_pic_parameter_set_id', ctypes.c_uint8),
    ('pps_seq_parameter_set_id', ctypes.c_uint8),
    ('sps_video_parameter_set_id', ctypes.c_uint8),
    ('num_extra_slice_header_bits', ctypes.c_uint8),
    ('num_ref_idx_l0_default_active_minus1', ctypes.c_uint8),
    ('num_ref_idx_l1_default_active_minus1', ctypes.c_uint8),
    ('init_qp_minus26', ctypes.c_int8),
    ('diff_cu_qp_delta_depth', ctypes.c_uint8),
    ('pps_cb_qp_offset', ctypes.c_int8),
    ('pps_cr_qp_offset', ctypes.c_int8),
    ('pps_beta_offset_div2', ctypes.c_int8),
    ('pps_tc_offset_div2', ctypes.c_int8),
    ('log2_parallel_merge_level_minus2', ctypes.c_uint8),
    ('log2_max_transform_skip_block_size_minus2', ctypes.c_uint8),
    ('diff_cu_chroma_qp_offset_depth', ctypes.c_uint8),
    ('chroma_qp_offset_list_len_minus1', ctypes.c_uint8),
    ('cb_qp_offset_list', ctypes.ARRAY(ctypes.c_int8, 6)),
    ('cr_qp_offset_list', ctypes.ARRAY(ctypes.c_int8, 6)),
    ('log2_sao_offset_scale_luma', ctypes.c_uint8),
    ('log2_sao_offset_scale_chroma', ctypes.c_uint8),
    ('pps_act_y_qp_offset_plus5', ctypes.c_int8),
    ('pps_act_cb_qp_offset_plus5', ctypes.c_int8),
    ('pps_act_cr_qp_offset_plus3', ctypes.c_int8),
    ('pps_num_palette_predictor_initializers', ctypes.c_uint8),
    ('luma_bit_depth_entry_minus8', ctypes.c_uint8),
    ('chroma_bit_depth_entry_minus8', ctypes.c_uint8),
    ('num_tile_columns_minus1', ctypes.c_uint8),
    ('num_tile_rows_minus1', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('reserved2', ctypes.c_uint8),
    ('column_width_minus1', ctypes.ARRAY(ctypes.c_uint16, 19)),
    ('row_height_minus1', ctypes.ARRAY(ctypes.c_uint16, 21)),
    ('reserved3', ctypes.c_uint32),
    ('pScalingLists', ctypes.POINTER(StdVideoH265ScalingLists)),
    ('pPredictorPaletteEntries', ctypes.POINTER(StdVideoH265PredictorPaletteEntries)),
]

StdVideoH265PictureParameterSet._type_ = {
    'flags': StdVideoH265PpsFlags,
    'pps_pic_parameter_set_id': ctypes.c_uint8,
    'pps_seq_parameter_set_id': ctypes.c_uint8,
    'sps_video_parameter_set_id': ctypes.c_uint8,
    'num_extra_slice_header_bits': ctypes.c_uint8,
    'num_ref_idx_l0_default_active_minus1': ctypes.c_uint8,
    'num_ref_idx_l1_default_active_minus1': ctypes.c_uint8,
    'init_qp_minus26': ctypes.c_int8,
    'diff_cu_qp_delta_depth': ctypes.c_uint8,
    'pps_cb_qp_offset': ctypes.c_int8,
    'pps_cr_qp_offset': ctypes.c_int8,
    'pps_beta_offset_div2': ctypes.c_int8,
    'pps_tc_offset_div2': ctypes.c_int8,
    'log2_parallel_merge_level_minus2': ctypes.c_uint8,
    'log2_max_transform_skip_block_size_minus2': ctypes.c_uint8,
    'diff_cu_chroma_qp_offset_depth': ctypes.c_uint8,
    'chroma_qp_offset_list_len_minus1': ctypes.c_uint8,
    'cb_qp_offset_list': ctypes.ARRAY(ctypes.c_int8, 6),
    'cr_qp_offset_list': ctypes.ARRAY(ctypes.c_int8, 6),
    'log2_sao_offset_scale_luma': ctypes.c_uint8,
    'log2_sao_offset_scale_chroma': ctypes.c_uint8,
    'pps_act_y_qp_offset_plus5': ctypes.c_int8,
    'pps_act_cb_qp_offset_plus5': ctypes.c_int8,
    'pps_act_cr_qp_offset_plus3': ctypes.c_int8,
    'pps_num_palette_predictor_initializers': ctypes.c_uint8,
    'luma_bit_depth_entry_minus8': ctypes.c_uint8,
    'chroma_bit_depth_entry_minus8': ctypes.c_uint8,
    'num_tile_columns_minus1': ctypes.c_uint8,
    'num_tile_rows_minus1': ctypes.c_uint8,
    'reserved1': ctypes.c_uint8,
    'reserved2': ctypes.c_uint8,
    'column_width_minus1': ctypes.ARRAY(ctypes.c_uint16, 19),
    'row_height_minus1': ctypes.ARRAY(ctypes.c_uint16, 21),
    'reserved3': ctypes.c_uint32,
    'pScalingLists': ctypes.POINTER(StdVideoH265ScalingLists),
    'pPredictorPaletteEntries': ctypes.POINTER(StdVideoH265PredictorPaletteEntries),
}
