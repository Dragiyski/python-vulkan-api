import ctypes

class VkVideoDecodeH264PictureInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdPictureInfo': ctypes.POINTER(StdVideoDecodeH264PictureInfo),
            'sliceCount': ctypes.c_uint32,
            'pSliceOffsets': ctypes.POINTER(ctypes.c_uint32),
        }


from .StdVideoDecodeH264PictureInfo import StdVideoDecodeH264PictureInfo

VkVideoDecodeH264PictureInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdPictureInfo', ctypes.POINTER(StdVideoDecodeH264PictureInfo)),
    ('sliceCount', ctypes.c_uint32),
    ('pSliceOffsets', ctypes.POINTER(ctypes.c_uint32)),
]
