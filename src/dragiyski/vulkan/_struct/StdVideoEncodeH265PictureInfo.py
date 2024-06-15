import ctypes, sys

class StdVideoEncodeH265PictureInfo(ctypes.Structure):
    pass

sys.modules[__name__] = StdVideoEncodeH265PictureInfo

from . import StdVideoEncodeH265PictureInfoFlags
from . import StdVideoEncodeH265LongTermRefPics
from . import StdVideoH265ShortTermRefPicSet
from . import StdVideoEncodeH265ReferenceListsInfo

StdVideoEncodeH265PictureInfo._fields_ = [
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
