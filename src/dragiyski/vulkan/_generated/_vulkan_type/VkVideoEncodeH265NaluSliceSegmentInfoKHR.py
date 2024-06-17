import ctypes, sys

class VkVideoEncodeH265NaluSliceSegmentInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH265NaluSliceSegmentInfoKHR

from . import StdVideoEncodeH265SliceSegmentHeader

VkVideoEncodeH265NaluSliceSegmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceSegmentHeader', ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader)),
]
