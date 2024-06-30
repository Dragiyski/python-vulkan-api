from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH265SequenceParameterSetVui'
_member_list_ = ['flags', 'aspect_ratio_idc', 'sar_width', 'sar_height', 'video_format', 'colour_primaries', 'transfer_characteristics', 'matrix_coeffs', 'chroma_sample_loc_type_top_field', 'chroma_sample_loc_type_bottom_field', 'reserved1', 'reserved2', 'def_disp_win_left_offset', 'def_disp_win_right_offset', 'def_disp_win_top_offset', 'def_disp_win_bottom_offset', 'vui_num_units_in_tick', 'vui_time_scale', 'vui_num_ticks_poc_diff_one_minus1', 'min_spatial_segmentation_idc', 'reserved3', 'max_bytes_per_pic_denom', 'max_bits_per_min_cu_denom', 'log2_max_mv_length_horizontal', 'log2_max_mv_length_vertical', 'pHrdParameters']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH265SpsVuiFlags'),
        'type_name': 'StdVideoH265SpsVuiFlags',
        'structure': 'StdVideoH265SpsVuiFlags',
        'is_string': False,
    },
    'aspect_ratio_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265AspectRatioIdc',
        'enum': 'StdVideoH265AspectRatioIdc',
        'is_string': False,
    },
    'sar_width': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'sar_height': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'video_format': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'colour_primaries': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'transfer_characteristics': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'matrix_coeffs': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'chroma_sample_loc_type_top_field': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'chroma_sample_loc_type_bottom_field': {
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
    'def_disp_win_left_offset': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'def_disp_win_right_offset': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'def_disp_win_top_offset': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'def_disp_win_bottom_offset': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'vui_num_units_in_tick': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vui_time_scale': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vui_num_ticks_poc_diff_one_minus1': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'min_spatial_segmentation_idc': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'reserved3': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'max_bytes_per_pic_denom': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'max_bits_per_min_cu_denom': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_max_mv_length_horizontal': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'log2_max_mv_length_vertical': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'pHrdParameters': {
        'type': CPointerType(CComplexType('StdVideoH265HrdParameters')),
        'type_name': 'StdVideoH265HrdParameters',
        'structure': 'StdVideoH265HrdParameters',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoH265HrdParameters',
    'StdVideoH265SpsVuiFlags',
}
_included_in_ = {
    'StdVideoH265SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
