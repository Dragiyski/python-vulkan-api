from ..._ctypes import *

_category_ = 'structure'
_name_ = 'StdVideoAV1TileInfo'
_member_list_ = ['flags', 'TileCols', 'TileRows', 'context_update_tile_id', 'tile_size_bytes_minus_1', 'reserved1', 'pMiColStarts', 'pMiRowStarts', 'pWidthInSbsMinus1', 'pHeightInSbsMinus1']
_member_info_ = {
    'flags': {
        'type': CComplexType('StdVideoAV1TileInfoFlags'),
        'type_name': 'StdVideoAV1TileInfoFlags',
        'structure': 'StdVideoAV1TileInfoFlags',
        'is_string': False,
    },
    'TileCols': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'TileRows': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'context_update_tile_id': {
        'type': CIntType('c_uint16'),
        'is_string': False,
    },
    'tile_size_bytes_minus_1': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'reserved1': {
        'type': CArrayType(CIntType('c_uint8'), 7),
        'is_string': False,
    },
    'pMiColStarts': {
        'type': CPointerType(CIntType('c_uint16')),
        'is_string': False,
    },
    'pMiRowStarts': {
        'type': CPointerType(CIntType('c_uint16')),
        'is_string': False,
    },
    'pWidthInSbsMinus1': {
        'type': CPointerType(CIntType('c_uint16')),
        'is_string': False,
    },
    'pHeightInSbsMinus1': {
        'type': CPointerType(CIntType('c_uint16')),
        'is_string': False,
    },
}
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
