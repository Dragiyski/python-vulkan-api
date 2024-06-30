from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoH264SequenceParameterSetVui'
_member_list_ = ['flags', 'aspect_ratio_idc', 'sar_width', 'sar_height', 'video_format', 'colour_primaries', 'transfer_characteristics', 'matrix_coefficients', 'num_units_in_tick', 'time_scale', 'max_num_reorder_frames', 'max_dec_frame_buffering', 'chroma_sample_loc_type_top_field', 'chroma_sample_loc_type_bottom_field', 'reserved1', 'pHrdParameters']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoH264SpsVuiFlags'),
        'type_name': 'StdVideoH264SpsVuiFlags',
        'structure': 'StdVideoH264SpsVuiFlags',
        'is_string': False,
    },
    'aspect_ratio_idc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264AspectRatioIdc',
        'enum': 'StdVideoH264AspectRatioIdc',
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
    'matrix_coefficients': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'num_units_in_tick': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'time_scale': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'max_num_reorder_frames': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'max_dec_frame_buffering': {
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
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pHrdParameters': {
        'type': CPointerType(CComplexType('StdVideoH264HrdParameters')),
        'type_name': 'StdVideoH264HrdParameters',
        'structure': 'StdVideoH264HrdParameters',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'StdVideoH264HrdParameters',
    'StdVideoH264SpsVuiFlags',
}
_included_in_ = {
    'StdVideoH264SequenceParameterSet',
}
_input_of_ = set()
_output_of_ = set()
