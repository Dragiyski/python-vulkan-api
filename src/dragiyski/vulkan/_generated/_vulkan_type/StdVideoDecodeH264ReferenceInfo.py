import ctypes

class StdVideoDecodeH264ReferenceInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': StdVideoDecodeH264ReferenceInfoFlags,
            'FrameNum': ctypes.c_uint16,
            'reserved': ctypes.c_uint16,
            'PicOrderCnt': ctypes.ARRAY(ctypes.c_int32, 2),
        }


from .StdVideoDecodeH264ReferenceInfoFlags import StdVideoDecodeH264ReferenceInfoFlags

StdVideoDecodeH264ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH264ReferenceInfoFlags),
    ('FrameNum', ctypes.c_uint16),
    ('reserved', ctypes.c_uint16),
    ('PicOrderCnt', ctypes.ARRAY(ctypes.c_int32, 2)),
]
