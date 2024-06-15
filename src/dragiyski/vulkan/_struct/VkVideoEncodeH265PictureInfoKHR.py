import ctypes, sys

class VkVideoEncodeH265PictureInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH265PictureInfoKHR

from . import StdVideoEncodeH265PictureInfo
from . import VkVideoEncodeH265NaluSliceSegmentInfoKHR

VkVideoEncodeH265PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceSegmentEntryCount', ctypes.c_uint32),
    ('pNaluSliceSegmentEntries', ctypes.POINTER(VkVideoEncodeH265NaluSliceSegmentInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH265PictureInfo)),
]
