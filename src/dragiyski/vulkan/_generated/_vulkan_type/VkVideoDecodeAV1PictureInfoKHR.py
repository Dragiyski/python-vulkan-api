import ctypes

class VkVideoDecodeAV1PictureInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdPictureInfo': ctypes.POINTER(StdVideoDecodeAV1PictureInfo),
            'referenceNameSlotIndices': ctypes.ARRAY(ctypes.c_int32, 7),
            'frameHeaderOffset': ctypes.c_uint32,
            'tileCount': ctypes.c_uint32,
            'pTileOffsets': ctypes.POINTER(ctypes.c_uint32),
            'pTileSizes': ctypes.POINTER(ctypes.c_uint32),
        }


from .StdVideoDecodeAV1PictureInfo import StdVideoDecodeAV1PictureInfo

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
