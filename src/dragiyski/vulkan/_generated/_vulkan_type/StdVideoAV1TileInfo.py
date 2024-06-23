import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1TileInfoFlags import CType as StdVideoAV1TileInfoFlags

CType._fields_ = [
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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoAV1TileInfoFlags',
    },
    'included_in': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoAV1TileInfoFlags'},
        'TileCols': {'python_name': ['tile', 'cols']},
        'TileRows': {'python_name': ['tile', 'rows']},
        'context_update_tile_id': {'python_name': ['context', 'update', 'tile', 'id']},
        'tile_size_bytes_minus_1': {'python_name': ['tile', 'size', 'bytes', 'minus', '1']},
        'reserved1': {'python_name': ['reserved1']},
        'pMiColStarts': {'python_name': ['p', 'mi', 'col', 'starts']},
        'pMiRowStarts': {'python_name': ['p', 'mi', 'row', 'starts']},
        'pWidthInSbsMinus1': {'python_name': ['p', 'width', 'in', 'sbs', 'minus1']},
        'pHeightInSbsMinus1': {'python_name': ['p', 'height', 'in', 'sbs', 'minus1']},
    }
}
