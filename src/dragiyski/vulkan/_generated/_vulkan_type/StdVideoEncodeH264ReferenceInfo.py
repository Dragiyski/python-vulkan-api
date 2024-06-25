import ctypes

class StdVideoEncodeH264ReferenceInfo(ctypes.Structure):
    pass

from .StdVideoEncodeH264ReferenceInfoFlags import StdVideoEncodeH264ReferenceInfoFlags

StdVideoEncodeH264ReferenceInfo._fields_ = [
    ('flags', StdVideoEncodeH264ReferenceInfoFlags),
    ('primary_pic_type', ctypes.c_int),
    ('FrameNum', ctypes.c_uint32),
    ('PicOrderCnt', ctypes.c_int32),
    ('long_term_pic_num', ctypes.c_uint16),
    ('long_term_frame_idx', ctypes.c_uint16),
    ('temporal_id', ctypes.c_uint8),
]

StdVideoEncodeH264ReferenceInfo._type_ = {
    'flags': StdVideoEncodeH264ReferenceInfoFlags,
    'primary_pic_type': ctypes.c_int,
    'FrameNum': ctypes.c_uint32,
    'PicOrderCnt': ctypes.c_int32,
    'long_term_pic_num': ctypes.c_uint16,
    'long_term_frame_idx': ctypes.c_uint16,
    'temporal_id': ctypes.c_uint8,
}
