import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH264PictureInfo import CType as StdVideoDecodeH264PictureInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH264PictureInfo)),
    ('sliceCount', ctypes.c_uint32),
    ('pSliceOffsets', ctypes.POINTER(ctypes.c_uint32)),
]
