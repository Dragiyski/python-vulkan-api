import ctypes, sys

class StdVideoAV1TileInfoFlags(ctypes.Structure):
    _fields_ = [
        ('uniform_tile_spacing_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

sys.modules[__name__] = StdVideoAV1TileInfoFlags
