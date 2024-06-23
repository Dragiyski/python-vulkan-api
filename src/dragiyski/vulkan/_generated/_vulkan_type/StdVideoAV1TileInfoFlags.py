import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('uniform_tile_spacing_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'StdVideoAV1TileInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'uniform_tile_spacing_flag': {'python_name': ['uniform', 'tile', 'spacing', 'flag']},
        'reserved': {'python_name': ['reserved']},
    }
}
