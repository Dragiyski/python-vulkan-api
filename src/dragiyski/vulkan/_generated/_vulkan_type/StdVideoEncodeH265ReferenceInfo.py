import ctypes

class StdVideoEncodeH265ReferenceInfo(ctypes.Structure):
    pass

from .StdVideoEncodeH265ReferenceInfoFlags import StdVideoEncodeH265ReferenceInfoFlags

StdVideoEncodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceInfoFlags),
    ('pic_type', ctypes.c_int),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
]

StdVideoEncodeH265ReferenceInfo._type_ = {
    'flags': StdVideoEncodeH265ReferenceInfoFlags,
    'pic_type': ctypes.c_int,
    'PicOrderCntVal': ctypes.c_int32,
    'TemporalId': ctypes.c_uint8,
}
