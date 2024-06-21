import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH264ReferenceInfoFlags import CType as StdVideoDecodeH264ReferenceInfoFlags

CType._fields_ = [
    ('flags', StdVideoDecodeH264ReferenceInfoFlags),
    ('FrameNum', ctypes.c_uint16),
    ('reserved', ctypes.c_uint16),
    ('PicOrderCnt', ctypes.ARRAY(ctypes.c_int32, 2)),
]
