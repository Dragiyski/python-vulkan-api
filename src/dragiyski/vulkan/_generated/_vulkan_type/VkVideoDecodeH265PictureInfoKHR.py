import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH265PictureInfo import CType as StdVideoDecodeH265PictureInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH265PictureInfo)),
    ('sliceSegmentCount', ctypes.c_uint32),
    ('pSliceSegmentOffsets', ctypes.POINTER(ctypes.c_uint32)),
]

descriptor = {
    'extends': {
        'VkVideoDecodeInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeH265PictureInfo',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_PICTURE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pStdPictureInfo': {'python_name': ['p', 'std', 'picture', 'info'], 'type': 'StdVideoDecodeH265PictureInfo'},
        'sliceSegmentCount': {'python_name': ['slice', 'segment', 'count']},
        'pSliceSegmentOffsets': {'python_name': ['p', 'slice', 'segment', 'offsets'], 'len': [['sliceSegmentCount']]},
    }
}
