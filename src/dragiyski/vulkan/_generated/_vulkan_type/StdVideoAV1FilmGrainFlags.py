import ctypes

class StdVideoAV1FilmGrainFlags(ctypes.Structure):
    _fields_ = [
        ('chroma_scaling_from_luma', ctypes.c_uint32, 1),
        ('overlap_flag', ctypes.c_uint32, 1),
        ('clip_to_restricted_range', ctypes.c_uint32, 1),
        ('update_grain', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 28),
    ]

StdVideoAV1FilmGrainFlags._type_ = {
    'chroma_scaling_from_luma': ctypes.c_uint32,
    'overlap_flag': ctypes.c_uint32,
    'clip_to_restricted_range': ctypes.c_uint32,
    'update_grain': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
