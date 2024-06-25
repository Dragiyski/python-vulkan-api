import ctypes

class StdVideoAV1TileInfoFlags(ctypes.Structure):
    _fields_ = [
        ('uniform_tile_spacing_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

StdVideoAV1TileInfoFlags._type_ = {
    'uniform_tile_spacing_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
