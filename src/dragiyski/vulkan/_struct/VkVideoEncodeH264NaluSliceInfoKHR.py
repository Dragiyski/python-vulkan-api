import ctypes, sys

class VkVideoEncodeH264NaluSliceInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH264NaluSliceInfoKHR

from . import StdVideoEncodeH264SliceHeader

VkVideoEncodeH264NaluSliceInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceHeader', ctypes.POINTER(StdVideoEncodeH264SliceHeader)),
]
