import ctypes

class StdVideoAV1TileInfoFlags(ctypes.Structure):
    _fields_ = [
        ('uniform_tile_spacing_flag', ctypes.c_uint32, 1),
        ('reserved', ctypes.c_uint32, 31),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'StdVideoAV1TileInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'uniform_tile_spacing_flag': 'uniform_tile_spacing_flag',
        'reserved': 'reserved',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'vulkan_video_codec_av1std',
    }
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

StdVideoAV1TileInfoFlags._type_ = {
    'uniform_tile_spacing_flag': ctypes.c_uint32,
    'reserved': ctypes.c_uint32,
}
