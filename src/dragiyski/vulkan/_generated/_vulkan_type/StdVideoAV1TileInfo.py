import ctypes

class StdVideoAV1TileInfo(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'StdVideoAV1TileInfoFlags',
    }
    _included_in_ = {
        'StdVideoDecodeAV1PictureInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'TileCols': 'tile_cols',
        'TileRows': 'tile_rows',
        'context_update_tile_id': 'context_update_tile_id',
        'tile_size_bytes_minus_1': 'tile_size_bytes_minus_1',
        'reserved1': 'reserved1',
        'pMiColStarts': 'mi_col_starts',
        'pMiRowStarts': 'mi_row_starts',
        'pWidthInSbsMinus1': 'width_in_sbs_minus1',
        'pHeightInSbsMinus1': 'height_in_sbs_minus1',
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


from .StdVideoAV1TileInfoFlags import StdVideoAV1TileInfoFlags

StdVideoAV1TileInfo._fields_ = [
    ('flags', StdVideoAV1TileInfoFlags),
    ('TileCols', ctypes.c_uint8),
    ('TileRows', ctypes.c_uint8),
    ('context_update_tile_id', ctypes.c_uint16),
    ('tile_size_bytes_minus_1', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('pMiColStarts', ctypes.POINTER(ctypes.c_uint16)),
    ('pMiRowStarts', ctypes.POINTER(ctypes.c_uint16)),
    ('pWidthInSbsMinus1', ctypes.POINTER(ctypes.c_uint16)),
    ('pHeightInSbsMinus1', ctypes.POINTER(ctypes.c_uint16)),
]

StdVideoAV1TileInfo._type_ = {
    'flags': StdVideoAV1TileInfoFlags,
    'TileCols': ctypes.c_uint8,
    'TileRows': ctypes.c_uint8,
    'context_update_tile_id': ctypes.c_uint16,
    'tile_size_bytes_minus_1': ctypes.c_uint8,
    'reserved1': ctypes.ARRAY(ctypes.c_uint8, 7),
    'pMiColStarts': ctypes.POINTER(ctypes.c_uint16),
    'pMiRowStarts': ctypes.POINTER(ctypes.c_uint16),
    'pWidthInSbsMinus1': ctypes.POINTER(ctypes.c_uint16),
    'pHeightInSbsMinus1': ctypes.POINTER(ctypes.c_uint16),
}
