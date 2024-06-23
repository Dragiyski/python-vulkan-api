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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH265LongTermRefPics',
        'StdVideoEncodeH265PictureInfoFlags',
        'StdVideoEncodeH265ReferenceListsInfo',
        'StdVideoH265ShortTermRefPicSet',
    },
    'included_in': {
        'VkVideoEncodeH265PictureInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH265PictureInfoFlags'},
        'pic_type': {'python_name': ['pic', 'type'], 'type': 'StdVideoH265PictureType'},
        'sps_video_parameter_set_id': {'python_name': ['sps', 'video', 'parameter', 'set', 'id']},
        'pps_seq_parameter_set_id': {'python_name': ['pps', 'seq', 'parameter', 'set', 'id']},
        'pps_pic_parameter_set_id': {'python_name': ['pps', 'pic', 'parameter', 'set', 'id']},
        'short_term_ref_pic_set_idx': {'python_name': ['short', 'term', 'ref', 'pic', 'set', 'idx']},
        'PicOrderCntVal': {'python_name': ['pic', 'order', 'cnt', 'val']},
        'TemporalId': {'python_name': ['temporal', 'id']},
        'reserved1': {'python_name': ['reserved1']},
        'pRefLists': {'python_name': ['p', 'ref', 'lists'], 'type': 'StdVideoEncodeH265ReferenceListsInfo'},
        'pShortTermRefPicSet': {'python_name': ['p', 'short', 'term', 'ref', 'pic', 'set'], 'type': 'StdVideoH265ShortTermRefPicSet'},
        'pLongTermRefPics': {'python_name': ['p', 'long', 'term', 'ref', 'pics'], 'type': 'StdVideoEncodeH265LongTermRefPics'},
    }
}
