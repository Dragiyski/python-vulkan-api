import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265LongTermRefPics import CType as StdVideoEncodeH265LongTermRefPics
from .StdVideoEncodeH265PictureInfoFlags import CType as StdVideoEncodeH265PictureInfoFlags
from .StdVideoEncodeH265ReferenceListsInfo import CType as StdVideoEncodeH265ReferenceListsInfo
from .StdVideoH265ShortTermRefPicSet import CType as StdVideoH265ShortTermRefPicSet

CType._fields_ = [
    ('flags', StdVideoEncodeH265PictureInfoFlags),
    ('pic_type', ctypes.c_int),
    ('sps_video_parameter_set_id', ctypes.c_uint8),
    ('pps_seq_parameter_set_id', ctypes.c_uint8),
    ('pps_pic_parameter_set_id', ctypes.c_uint8),
    ('short_term_ref_pic_set_idx', ctypes.c_uint8),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
    ('reserved1', ctypes.ARRAY(ctypes.c_uint8, 7)),
    ('pRefLists', ctypes.POINTER(StdVideoEncodeH265ReferenceListsInfo)),
    ('pShortTermRefPicSet', ctypes.POINTER(StdVideoH265ShortTermRefPicSet)),
    ('pLongTermRefPics', ctypes.POINTER(StdVideoEncodeH265LongTermRefPics)),
]
