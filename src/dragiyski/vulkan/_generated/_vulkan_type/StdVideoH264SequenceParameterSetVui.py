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
