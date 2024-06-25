import ctypes

class VkVideoEncodeH265NaluSliceSegmentInfoKHR(ctypes.Structure):
    pass

from .StdVideoEncodeH265SliceSegmentHeader import StdVideoEncodeH265SliceSegmentHeader

VkVideoEncodeH265NaluSliceSegmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceSegmentHeader', ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader)),
]

VkVideoEncodeH265NaluSliceSegmentInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'constantQp': ctypes.c_int32,
    'pStdSliceSegmentHeader': ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader),
}
