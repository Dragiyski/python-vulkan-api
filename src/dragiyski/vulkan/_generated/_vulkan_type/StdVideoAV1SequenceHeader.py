import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1ColorConfig import CType as StdVideoAV1ColorConfig
from .StdVideoAV1SequenceHeaderFlags import CType as StdVideoAV1SequenceHeaderFlags
from .StdVideoAV1TimingInfo import CType as StdVideoAV1TimingInfo

CType._fields_ = [
    ('flags', StdVideoAV1SequenceHeaderFlags),
    ('seq_profile', ctypes.c_int),
    ('frame_width_bits_minus_1', ctypes.c_uint8),
    ('frame_height_bits_minus_1', ctypes.c_uint8),
    ('max_frame_width_minus_1', ctypes.c_uint16),
    ('max_frame_height_minus_1', ctypes.c_uint16),
    ('delta_frame_id_length_minus_2', ctypes.c_uint8),
    ('additional_frame_id_length_minus_1', ctypes.c_uint8),
    ('order_hint_bits_minus_1', ctypes.c_uint8),
    ('seq_force_integer_mv', ctypes.c_uint8),
    ('seq_force_screen_content_tools', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 5)),
    ('pColorConfig', ctypes.POINTER(StdVideoAV1ColorConfig)),
    ('pTimingInfo', ctypes.POINTER(StdVideoAV1TimingInfo)),
]