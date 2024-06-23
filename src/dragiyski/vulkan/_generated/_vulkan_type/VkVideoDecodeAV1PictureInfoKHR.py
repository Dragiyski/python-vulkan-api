import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeAV1PictureInfo import CType as StdVideoDecodeAV1PictureInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeAV1PictureInfo)),
    ('referenceNameSlotIndices', ctypes.ARRAY(ctypes.c_int32, 7)),
    ('frameHeaderOffset', ctypes.c_uint32),
    ('tileCount', ctypes.c_uint32),
    ('pTileOffsets', ctypes.POINTER(ctypes.c_uint32)),
    ('pTileSizes', ctypes.POINTER(ctypes.c_uint32)),
]

descriptor = {
    'extends': {
        'VkVideoDecodeInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeAV1PictureInfo',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_PICTURE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pStdPictureInfo': {'python_name': ['p', 'std', 'picture', 'info'], 'type': 'StdVideoDecodeAV1PictureInfo'},
        'referenceNameSlotIndices': {'python_name': ['reference', 'name', 'slot', 'indices']},
        'frameHeaderOffset': {'python_name': ['frame', 'header', 'offset']},
        'tileCount': {'python_name': ['tile', 'count']},
        'pTileOffsets': {'python_name': ['p', 'tile', 'offsets'], 'len': [['tileCount']]},
        'pTileSizes': {'python_name': ['p', 'tile', 'sizes'], 'len': [['tileCount']]},
    }
}
