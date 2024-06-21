import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH265PictureInfo import CType as StdVideoDecodeH265PictureInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH265PictureInfo)),
    ('sliceSegmentCount', ctypes.c_uint32),
    ('pSliceSegmentOffsets', ctypes.POINTER(ctypes.c_uint32)),
]
