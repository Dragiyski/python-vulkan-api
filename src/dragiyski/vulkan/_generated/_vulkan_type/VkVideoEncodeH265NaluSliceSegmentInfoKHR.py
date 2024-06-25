import ctypes

class VkVideoEncodeH265NaluSliceSegmentInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'constantQp': ctypes.c_int32,
            'pStdSliceSegmentHeader': ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader),
        }


from .StdVideoEncodeH265SliceSegmentHeader import StdVideoEncodeH265SliceSegmentHeader

VkVideoEncodeH265NaluSliceSegmentInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceSegmentHeader', ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader)),
]
