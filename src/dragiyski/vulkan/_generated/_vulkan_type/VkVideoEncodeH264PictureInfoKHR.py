import ctypes

class VkVideoEncodeH264PictureInfoKHR(ctypes.Structure):
    pass

from .StdVideoEncodeH264PictureInfo import StdVideoEncodeH264PictureInfo
from .VkVideoEncodeH264NaluSliceInfoKHR import VkVideoEncodeH264NaluSliceInfoKHR

VkVideoEncodeH264PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceEntryCount', ctypes.c_uint32),
    ('pNaluSliceEntries', ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH264PictureInfo)),
    ('generatePrefixNalu', ctypes.c_uint32),
]

VkVideoEncodeH264PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'naluSliceEntryCount': ctypes.c_uint32,
    'pNaluSliceEntries': ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR),
    'pStdPictureInfo': ctypes.POINTER(StdVideoEncodeH264PictureInfo),
    'generatePrefixNalu': ctypes.c_uint32,
}
