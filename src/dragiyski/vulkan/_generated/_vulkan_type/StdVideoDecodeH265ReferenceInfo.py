import ctypes

class StdVideoDecodeH265ReferenceInfo(ctypes.Structure):
    pass

from .StdVideoDecodeH265ReferenceInfoFlags import StdVideoDecodeH265ReferenceInfoFlags

StdVideoDecodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH265ReferenceInfoFlags),
    ('PicOrderCntVal', ctypes.c_int32),
]

StdVideoDecodeH265ReferenceInfo._type_ = {
    'flags': StdVideoDecodeH265ReferenceInfoFlags,
    'PicOrderCntVal': ctypes.c_int32,
}
