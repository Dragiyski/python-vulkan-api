import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH264HrdParameters import CType as StdVideoH264HrdParameters
from .StdVideoH264SpsVuiFlags import CType as StdVideoH264SpsVuiFlags

CType._fields_ = [
    ('flags', StdVideoH264SpsVuiFlags),
    ('aspect_ratio_idc', ctypes.c_int),
    ('sar_width', ctypes.c_uint16),
    ('sar_height', ctypes.c_uint16),
    ('video_format', ctypes.c_uint8),
    ('colour_primaries', ctypes.c_uint8),
    ('transfer_characteristics', ctypes.c_uint8),
    ('matrix_coefficients', ctypes.c_uint8),
    ('num_units_in_tick', ctypes.c_uint32),
    ('time_scale', ctypes.c_uint32),
    ('max_num_reorder_frames', ctypes.c_uint8),
    ('max_dec_frame_buffering', ctypes.c_uint8),
    ('chroma_sample_loc_type_top_field', ctypes.c_uint8),
    ('chroma_sample_loc_type_bottom_field', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint32),
    ('pHrdParameters', ctypes.POINTER(StdVideoH264HrdParameters)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoH264HrdParameters',
        'StdVideoH264SpsVuiFlags',
    },
    'included_in': {
        'StdVideoH264SequenceParameterSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoH264SpsVuiFlags'},
        'aspect_ratio_idc': {'python_name': ['aspect', 'ratio', 'idc'], 'type': 'StdVideoH264AspectRatioIdc'},
        'sar_width': {'python_name': ['sar', 'width']},
        'sar_height': {'python_name': ['sar', 'height']},
        'video_format': {'python_name': ['video', 'format']},
        'colour_primaries': {'python_name': ['colour', 'primaries']},
        'transfer_characteristics': {'python_name': ['transfer', 'characteristics']},
        'matrix_coefficients': {'python_name': ['matrix', 'coefficients']},
        'num_units_in_tick': {'python_name': ['num', 'units', 'in', 'tick']},
        'time_scale': {'python_name': ['time', 'scale']},
        'max_num_reorder_frames': {'python_name': ['max', 'num', 'reorder', 'frames']},
        'max_dec_frame_buffering': {'python_name': ['max', 'dec', 'frame', 'buffering']},
        'chroma_sample_loc_type_top_field': {'python_name': ['chroma', 'sample', 'loc', 'type', 'top', 'field']},
        'chroma_sample_loc_type_bottom_field': {'python_name': ['chroma', 'sample', 'loc', 'type', 'bottom', 'field']},
        'reserved1': {'python_name': ['reserved1']},
        'pHrdParameters': {'python_name': ['p', 'hrd', 'parameters'], 'type': 'StdVideoH264HrdParameters'},
    }
}
