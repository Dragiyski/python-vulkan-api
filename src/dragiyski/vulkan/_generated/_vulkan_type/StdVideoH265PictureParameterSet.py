import ctypes, sys

class StdVideoH265PictureParameterSet(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoH265PictureParameterSet

from . import StdVideoH265PpsFlags
from . import StdVideoH265PredictorPaletteEntries
from . import StdVideoH265ScalingLists

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
