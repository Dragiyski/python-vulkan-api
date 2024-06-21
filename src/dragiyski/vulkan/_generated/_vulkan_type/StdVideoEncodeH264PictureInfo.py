import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264PictureInfoFlags import CType as StdVideoEncodeH264PictureInfoFlags
from .StdVideoEncodeH264ReferenceListsInfo import CType as StdVideoEncodeH264ReferenceListsInfo

CType._fields_ = [
    ('flags', StdVideoEncodeH264PictureInfoFlags),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('pic_parameter_set_id', ctypes.c_uint8),
    ('idr_pic_id', ctypes.c_uint16),
    ('primary_pic_type', ctypes.c_int),
    ('frame_num', ctypes.c_uint32),
    ('PicOrderCnt', ctypes.c_int32),
    ('temporal_id', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 3)),
    ('pRefLists', ctypes.POINTER(StdVideoEncodeH264ReferenceListsInfo)),
]
