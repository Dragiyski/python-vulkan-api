import ctypes

class StdVideoAV1TileInfoFlags(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'uniform_tile_spacing_flag': ctypes.c_uint32,
            'reserved': ctypes.c_uint32,
        }

    _fields_ = [
        ('uniform_tile_spacing_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]
