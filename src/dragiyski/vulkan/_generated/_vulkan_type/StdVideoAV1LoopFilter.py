import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1LoopFilterFlags import CType as StdVideoAV1LoopFilterFlags

CType._fields_ = [
    ('flags', StdVideoAV1LoopFilterFlags),
    ('loop_filter_level', ctypes.ARRAY(ctypes.c_uint8, 4)),
    ('loop_filter_sharpness', ctypes.c_uint8),
    ('update_ref_delta', ctypes.c_uint8),
    ('loop_filter_ref_deltas', ctypes.ARRAY(ctypes.c_int8, 8)),
    ('update_mode_delta', ctypes.c_uint8),
    ('loop_filter_mode_deltas', ctypes.ARRAY(ctypes.c_int8, 2)),
]
