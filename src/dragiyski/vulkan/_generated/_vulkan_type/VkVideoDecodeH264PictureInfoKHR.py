import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH264PictureInfo import CType as StdVideoDecodeH264PictureInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH264PictureInfo)),
    ('sliceCount', ctypes.c_uint32),
    ('pSliceOffsets', ctypes.POINTER(ctypes.c_uint32)),
]

descriptor = {
    'extends': {
        'VkVideoDecodeInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeH264PictureInfo',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_PICTURE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pStdPictureInfo': {'python_name': ['p', 'std', 'picture', 'info'], 'type': 'StdVideoDecodeH264PictureInfo'},
        'sliceCount': {'python_name': ['slice', 'count']},
        'pSliceOffsets': {'python_name': ['p', 'slice', 'offsets'], 'len': [['sliceCount']]},
    }
}
