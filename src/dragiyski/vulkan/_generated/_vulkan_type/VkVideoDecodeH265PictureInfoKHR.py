import ctypes

class VkVideoDecodeH265PictureInfoKHR(ctypes.Structure):
    pass

from .StdVideoDecodeH265PictureInfo import StdVideoDecodeH265PictureInfo

VkVideoDecodeH265PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH265PictureInfo)),
    ('sliceSegmentCount', ctypes.c_uint32),
    ('pSliceSegmentOffsets', ctypes.POINTER(ctypes.c_uint32)),
]

VkVideoDecodeH265PictureInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdPictureInfo': ctypes.POINTER(StdVideoDecodeH265PictureInfo),
    'sliceSegmentCount': ctypes.c_uint32,
    'pSliceSegmentOffsets': ctypes.POINTER(ctypes.c_uint32),
}
