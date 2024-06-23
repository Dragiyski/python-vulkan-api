import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264PictureInfo import CType as StdVideoEncodeH264PictureInfo
from .VkVideoEncodeH264NaluSliceInfoKHR import CType as VkVideoEncodeH264NaluSliceInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceEntryCount', ctypes.c_uint32),
    ('pNaluSliceEntries', ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH264PictureInfo)),
    ('generatePrefixNalu', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkVideoEncodeInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264PictureInfo',
        'VkVideoEncodeH264NaluSliceInfoKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_PICTURE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'naluSliceEntryCount': {'python_name': ['nalu', 'slice', 'entry', 'count']},
        'pNaluSliceEntries': {'python_name': ['p', 'nalu', 'slice', 'entries'], 'len': [['naluSliceEntryCount']], 'type': 'VkVideoEncodeH264NaluSliceInfoKHR'},
        'pStdPictureInfo': {'python_name': ['p', 'std', 'picture', 'info'], 'type': 'StdVideoEncodeH264PictureInfo'},
        'generatePrefixNalu': {'python_name': ['generate', 'prefix', 'nalu']},
    }
}
