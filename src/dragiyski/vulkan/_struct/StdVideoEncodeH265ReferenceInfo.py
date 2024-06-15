import ctypes, sys

class StdVideoEncodeH265ReferenceInfo(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoEncodeH265ReferenceInfo

from . import StdVideoEncodeH265ReferenceInfoFlags

StdVideoEncodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceInfoFlags),
    ('pic_type', ctypes.c_int),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
]
