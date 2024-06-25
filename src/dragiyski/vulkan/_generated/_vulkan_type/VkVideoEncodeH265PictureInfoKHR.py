import ctypes

class VkVideoEncodeH265PictureInfoKHR(ctypes.Structure):
    pass

from .StdVideoEncodeH265PictureInfo import StdVideoEncodeH265PictureInfo
from .VkVideoEncodeH265NaluSliceSegmentInfoKHR import VkVideoEncodeH265NaluSliceSegmentInfoKHR

VkVideoEncodeH265PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceSegmentEntryCount', ctypes.c_uint32),
    ('pNaluSliceSegmentEntries', ctypes.POINTER(VkVideoEncodeH265NaluSliceSegmentInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH265PictureInfo)),
]

VkVideoEncodeH265PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'naluSliceSegmentEntryCount': ctypes.c_uint32,
    'pNaluSliceSegmentEntries': ctypes.POINTER(VkVideoEncodeH265NaluSliceSegmentInfoKHR),
    'pStdPictureInfo': ctypes.POINTER(StdVideoEncodeH265PictureInfo),
}
