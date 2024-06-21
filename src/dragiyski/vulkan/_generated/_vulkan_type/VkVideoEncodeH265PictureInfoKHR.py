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
