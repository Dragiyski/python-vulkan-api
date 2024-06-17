import ctypes, sys

class StdVideoDecodeH265ReferenceInfo(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoDecodeH265ReferenceInfo

from . import StdVideoDecodeH265ReferenceInfoFlags

StdVideoDecodeH265ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH265ReferenceInfoFlags),
    ('PicOrderCntVal', ctypes.c_int32),
]
