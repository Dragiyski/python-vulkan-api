import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('chroma_scaling_from_luma', ctypes.c_uint32, 1),
        ('overlap_flag', ctypes.c_uint32, 1),
        ('clip_to_restricted_range', ctypes.c_uint32, 1),
        ('update_grain', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 28),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoAV1FilmGrain',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'chroma_scaling_from_luma': {'python_name': ['chroma', 'scaling', 'from', 'luma']},
        'overlap_flag': {'python_name': ['overlap', 'flag']},
        'clip_to_restricted_range': {'python_name': ['clip', 'to', 'restricted', 'range']},
        'update_grain': {'python_name': ['update', 'grain']},
        'reserved': {'python_name': ['reserved']},
    }
}
