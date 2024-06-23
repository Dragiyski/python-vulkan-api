import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265HrdParameters import CType as StdVideoH265HrdParameters
from .StdVideoH265SpsVuiFlags import CType as StdVideoH265SpsVuiFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH265HrdParameters',
        'StdVideoH265SpsVuiFlags',
    },
    'included_in': {
        'StdVideoH265SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH265SpsVuiFlags'},
        'aspect_ratio_idc': {'python_name': ['aspect', 'ratio', 'idc'], 'type': 'StdVideoH265AspectRatioIdc'},
        'sar_width': {'python_name': ['sar', 'width']},
        'sar_height': {'python_name': ['sar', 'height']},
        'video_format': {'python_name': ['video', 'format']},
        'colour_primaries': {'python_name': ['colour', 'primaries']},
        'transfer_characteristics': {'python_name': ['transfer', 'characteristics']},
        'matrix_coeffs': {'python_name': ['matrix', 'coeffs']},
        'chroma_sample_loc_type_top_field': {'python_name': ['chroma', 'sample', 'loc', 'type', 'top', 'field']},
        'chroma_sample_loc_type_bottom_field': {'python_name': ['chroma', 'sample', 'loc', 'type', 'bottom', 'field']},
        'reserved1': {'python_name': ['reserved1']},
        'reserved2': {'python_name': ['reserved2']},
        'def_disp_win_left_offset': {'python_name': ['def', 'disp', 'win', 'left', 'offset']},
        'def_disp_win_right_offset': {'python_name': ['def', 'disp', 'win', 'right', 'offset']},
        'def_disp_win_top_offset': {'python_name': ['def', 'disp', 'win', 'top', 'offset']},
        'def_disp_win_bottom_offset': {'python_name': ['def', 'disp', 'win', 'bottom', 'offset']},
        'vui_num_units_in_tick': {'python_name': ['vui', 'num', 'units', 'in', 'tick']},
        'vui_time_scale': {'python_name': ['vui', 'time', 'scale']},
        'vui_num_ticks_poc_diff_one_minus1': {'python_name': ['vui', 'num', 'ticks', 'poc', 'diff', 'one', 'minus1']},
        'min_spatial_segmentation_idc': {'python_name': ['min', 'spatial', 'segmentation', 'idc']},
        'reserved3': {'python_name': ['reserved3']},
        'max_bytes_per_pic_denom': {'python_name': ['max', 'bytes', 'per', 'pic', 'denom']},
        'max_bits_per_min_cu_denom': {'python_name': ['max', 'bits', 'per', 'min', 'cu', 'denom']},
        'log2_max_mv_length_horizontal': {'python_name': ['log2', 'max', 'mv', 'length', 'horizontal']},
        'log2_max_mv_length_vertical': {'python_name': ['log2', 'max', 'mv', 'length', 'vertical']},
        'pHrdParameters': {'python_name': ['p', 'hrd', 'parameters'], 'type': 'StdVideoH265HrdParameters'},
    }
}
