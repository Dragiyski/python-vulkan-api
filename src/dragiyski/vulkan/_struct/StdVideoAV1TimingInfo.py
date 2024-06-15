import ctypes, sys

class StdVideoAV1TimingInfo(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoAV1TimingInfo

from . import StdVideoAV1TimingInfoFlags

StdVideoAV1TimingInfo._fields_ = [
    ('flags', StdVideoAV1TimingInfoFlags),
    ('num_units_in_display_tick', ctypes.c_uint32),
    ('time_scale', ctypes.c_uint32),
    ('num_ticks_per_picture_minus_1', ctypes.c_uint32),
]
