import ctypes

class StdVideoAV1TileInfo(ctypes.Structure):
    pass

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
