import ctypes

class StdVideoDecodeH264ReferenceInfo(ctypes.Structure):
    pass

from .StdVideoDecodeH264ReferenceInfoFlags import StdVideoDecodeH264ReferenceInfoFlags

StdVideoDecodeH264ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH264ReferenceInfoFlags),
    ('FrameNum', ctypes.c_uint16),
    ('reserved', ctypes.c_uint16),
    ('PicOrderCnt', ctypes.ARRAY(ctypes.c_int32, 2)),
]

StdVideoDecodeH264ReferenceInfo._type_ = {
    'flags': StdVideoDecodeH264ReferenceInfoFlags,
    'FrameNum': ctypes.c_uint16,
    'reserved': ctypes.c_uint16,
    'PicOrderCnt': ctypes.ARRAY(ctypes.c_int32, 2),
}
