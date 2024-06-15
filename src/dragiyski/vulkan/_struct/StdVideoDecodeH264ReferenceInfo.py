import ctypes, sys

class StdVideoDecodeH264ReferenceInfo(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoDecodeH264ReferenceInfo

from . import StdVideoDecodeH264ReferenceInfoFlags

StdVideoDecodeH264ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeH264ReferenceInfoFlags),
    ('FrameNum', ctypes.c_uint16),
    ('reserved', ctypes.c_uint16),
    ('PicOrderCnt', ctypes.ARRAY(ctypes.c_int32, 2)),
]
