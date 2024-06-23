import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265PictureInfo import CType as StdVideoEncodeH265PictureInfo
from .VkVideoEncodeH265NaluSliceSegmentInfoKHR import CType as VkVideoEncodeH265NaluSliceSegmentInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceSegmentEntryCount', ctypes.c_uint32),
    ('pNaluSliceSegmentEntries', ctypes.POINTER(VkVideoEncodeH265NaluSliceSegmentInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH265PictureInfo)),
]

descriptor = {
    'extends': {
        'VkVideoEncodeInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH265PictureInfo',
        'VkVideoEncodeH265NaluSliceSegmentInfoKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_PICTURE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'naluSliceSegmentEntryCount': {'python_name': ['nalu', 'slice', 'segment', 'entry', 'count']},
        'pNaluSliceSegmentEntries': {'python_name': ['p', 'nalu', 'slice', 'segment', 'entries'], 'len': [['naluSliceSegmentEntryCount']], 'type': 'VkVideoEncodeH265NaluSliceSegmentInfoKHR'},
        'pStdPictureInfo': {'python_name': ['p', 'std', 'picture', 'info'], 'type': 'StdVideoEncodeH265PictureInfo'},
    }
}
