import ctypes

class VkVideoDecodeH264PictureInfoKHR(ctypes.Structure):
    pass

from .StdVideoDecodeH264PictureInfo import StdVideoDecodeH264PictureInfo

VkVideoDecodeH264PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH264PictureInfo)),
    ('sliceCount', ctypes.c_uint32),
    ('pSliceOffsets', ctypes.POINTER(ctypes.c_uint32)),
]

VkVideoDecodeH264PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdPictureInfo': ctypes.POINTER(StdVideoDecodeH264PictureInfo),
    'sliceCount': ctypes.c_uint32,
    'pSliceOffsets': ctypes.POINTER(ctypes.c_uint32),
}
