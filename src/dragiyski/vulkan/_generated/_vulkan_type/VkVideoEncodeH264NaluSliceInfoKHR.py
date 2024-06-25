import ctypes

class VkVideoEncodeH264NaluSliceInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'constantQp': ctypes.c_int32,
            'pStdSliceHeader': ctypes.POINTER(StdVideoEncodeH264SliceHeader),
        }


from .StdVideoEncodeH264SliceHeader import StdVideoEncodeH264SliceHeader

VkVideoEncodeH264NaluSliceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceHeader', ctypes.POINTER(StdVideoEncodeH264SliceHeader)),
]
