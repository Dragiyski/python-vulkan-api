import ctypes, sys

class VkVideoDecodeAV1PictureInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeAV1PictureInfoKHR

from . import StdVideoDecodeAV1PictureInfo

VkVideoDecodeAV1PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeAV1PictureInfo)),
    ('referenceNameSlotIndices', ctypes.ARRAY(ctypes.c_int32, 7)),
    ('frameHeaderOffset', ctypes.c_uint32),
    ('tileCount', ctypes.c_uint32),
    ('pTileOffsets', ctypes.POINTER(ctypes.c_uint32)),
    ('pTileSizes', ctypes.POINTER(ctypes.c_uint32)),
]
