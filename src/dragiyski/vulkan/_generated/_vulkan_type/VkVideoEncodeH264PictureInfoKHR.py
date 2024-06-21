import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264PictureInfo import CType as StdVideoEncodeH264PictureInfo
from .VkVideoEncodeH264NaluSliceInfoKHR import CType as VkVideoEncodeH264NaluSliceInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('naluSliceEntryCount', ctypes.c_uint32),
    ('pNaluSliceEntries', ctypes.POINTER(VkVideoEncodeH264NaluSliceInfoKHR)),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoEncodeH264PictureInfo)),
    ('generatePrefixNalu', ctypes.c_uint32),
]
