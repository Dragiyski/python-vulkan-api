import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265ReferenceInfoFlags import CType as StdVideoEncodeH265ReferenceInfoFlags

CType._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceInfoFlags),
    ('pic_type', ctypes.c_int),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
]
