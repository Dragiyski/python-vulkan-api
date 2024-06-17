import ctypes, sys

class StdVideoAV1LoopFilter(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoAV1LoopFilter

from . import StdVideoAV1LoopFilterFlags

StdVideoAV1LoopFilter._fields_ = [
    ('flags', StdVideoAV1LoopFilterFlags),
    ('loop_filter_level', ctypes.ARRAY(ctypes.c_uint8, 4)),
    ('loop_filter_sharpness', ctypes.c_uint8),
    ('update_ref_delta', ctypes.c_uint8),
    ('loop_filter_ref_deltas', ctypes.ARRAY(ctypes.c_int8, 8)),
    ('update_mode_delta', ctypes.c_uint8),
    ('loop_filter_mode_deltas', ctypes.ARRAY(ctypes.c_int8, 2)),
]
