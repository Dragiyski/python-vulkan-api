import ctypes

class StdVideoH265SequenceParameterSetVui(ctypes.Structure):
    pass

from .StdVideoH265HrdParameters import StdVideoH265HrdParameters
from .StdVideoH265SpsVuiFlags import StdVideoH265SpsVuiFlags

StdVideoH265SequenceParameterSetVui._fields_ = [
    ('flags', StdVideoH265SpsVuiFlags),
    ('aspect_ratio_idc', ctypes.c_int),
    ('sar_width', ctypes.c_uint16),
    ('sar_height', ctypes.c_uint16),
    ('video_format', ctypes.c_uint8),
    ('colour_primaries', ctypes.c_uint8),
    ('transfer_characteristics', ctypes.c_uint8),
    ('matrix_coeffs', ctypes.c_uint8),
    ('chroma_sample_loc_type_top_field', ctypes.c_uint8),
    ('chroma_sample_loc_type_bottom_field', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('reserved2', ctypes.c_uint8),
    ('def_disp_win_left_offset', ctypes.c_uint16),
    ('def_disp_win_right_offset', ctypes.c_uint16),
    ('def_disp_win_top_offset', ctypes.c_uint16),
    ('def_disp_win_bottom_offset', ctypes.c_uint16),
    ('vui_num_units_in_tick', ctypes.c_uint32),
    ('vui_time_scale', ctypes.c_uint32),
    ('vui_num_ticks_poc_diff_one_minus1', ctypes.c_uint32),
    ('min_spatial_segmentation_idc', ctypes.c_uint16),
    ('reserved3', ctypes.c_uint16),
    ('max_bytes_per_pic_denom', ctypes.c_uint8),
    ('max_bits_per_min_cu_denom', ctypes.c_uint8),
    ('log2_max_mv_length_horizontal', ctypes.c_uint8),
    ('log2_max_mv_length_vertical', ctypes.c_uint8),
    ('pHrdParameters', ctypes.POINTER(StdVideoH265HrdParameters)),
]

StdVideoH265SequenceParameterSetVui._type_ = {
    'flags': StdVideoH265SpsVuiFlags,
    'aspect_ratio_idc': ctypes.c_int,
    'sar_width': ctypes.c_uint16,
    'sar_height': ctypes.c_uint16,
    'video_format': ctypes.c_uint8,
    'colour_primaries': ctypes.c_uint8,
    'transfer_characteristics': ctypes.c_uint8,
    'matrix_coeffs': ctypes.c_uint8,
    'chroma_sample_loc_type_top_field': ctypes.c_uint8,
    'chroma_sample_loc_type_bottom_field': ctypes.c_uint8,
    'reserved1': ctypes.c_uint8,
    'reserved2': ctypes.c_uint8,
    'def_disp_win_left_offset': ctypes.c_uint16,
    'def_disp_win_right_offset': ctypes.c_uint16,
    'def_disp_win_top_offset': ctypes.c_uint16,
    'def_disp_win_bottom_offset': ctypes.c_uint16,
    'vui_num_units_in_tick': ctypes.c_uint32,
    'vui_time_scale': ctypes.c_uint32,
    'vui_num_ticks_poc_diff_one_minus1': ctypes.c_uint32,
    'min_spatial_segmentation_idc': ctypes.c_uint16,
    'reserved3': ctypes.c_uint16,
    'max_bytes_per_pic_denom': ctypes.c_uint8,
    'max_bits_per_min_cu_denom': ctypes.c_uint8,
    'log2_max_mv_length_horizontal': ctypes.c_uint8,
    'log2_max_mv_length_vertical': ctypes.c_uint8,
    'pHrdParameters': ctypes.POINTER(StdVideoH265HrdParameters),
}
