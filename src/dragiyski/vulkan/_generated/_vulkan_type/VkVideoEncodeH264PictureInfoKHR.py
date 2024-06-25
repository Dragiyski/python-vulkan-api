import ctypes

class VkVideoEncodeH264PictureInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'naluSliceEntryCount': ctypes.c_uint32,
            'pNaluSliceEntries': ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR),
            'pStdPictureInfo': ctypes.POINTER(StdVideoEncodeH264PictureInfo),
            'generatePrefixNalu': ctypes.c_uint32,
        }


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
