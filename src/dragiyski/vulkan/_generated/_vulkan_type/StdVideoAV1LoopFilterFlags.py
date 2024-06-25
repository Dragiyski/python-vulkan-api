import ctypes

class StdVideoAV1LoopFilterFlags(ctypes.Structure):
    _fields_ = [
        ('loop_filter_delta_enabled', ctypes.c_uint32, 1),
        ('loop_filter_delta_update', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 30),
    ]

StdVideoAV1LoopFilterFlags._type_ = {
    'loop_filter_delta_enabled': ctypes.c_uint32,
    'loop_filter_delta_update': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
