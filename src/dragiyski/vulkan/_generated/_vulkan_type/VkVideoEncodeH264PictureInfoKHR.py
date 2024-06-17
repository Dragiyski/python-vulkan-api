import ctypes, sys

class VkVideoEncodeH264PictureInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH264PictureInfoKHR

from . import StdVideoEncodeH264PictureInfo
from . import VkVideoEncodeH264NaluSliceInfoKHR

VkVideoEncodeH264PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceEntryCount', ctypes.c_uint32),
    ('pNaluSliceEntries', ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH264PictureInfo)),
    ('generatePrefixNalu', ctypes.c_uint32),
]
