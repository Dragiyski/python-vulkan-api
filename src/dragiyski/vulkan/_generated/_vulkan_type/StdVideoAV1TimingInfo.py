import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1TimingInfoFlags import CType as StdVideoAV1TimingInfoFlags

CType._fields_ = [
    ('flags', StdVideoAV1TimingInfoFlags),
    ('num_units_in_display_tick', ctypes.c_uint32),
    ('time_scale', ctypes.c_uint32),
    ('num_ticks_per_picture_minus_1', ctypes.c_uint32),
]
