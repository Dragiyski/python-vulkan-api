import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH265ReferenceInfoFlags import CType as StdVideoDecodeH265ReferenceInfoFlags

CType._fields_ = [
    ('flags', StdVideoDecodeH265ReferenceInfoFlags),
    ('PicOrderCntVal', ctypes.c_int32),
]
