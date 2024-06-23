import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264ReferenceInfoFlags import CType as StdVideoEncodeH264ReferenceInfoFlags

CType._fields_ = [
    ('flags', StdVideoEncodeH264ReferenceInfoFlags),
    ('primary_pic_type', ctypes.c_int),
    ('FrameNum', ctypes.c_uint32),
    ('PicOrderCnt', ctypes.c_int32),
    ('long_term_pic_num', ctypes.c_uint16),
    ('long_term_frame_idx', ctypes.c_uint16),
    ('temporal_id', ctypes.c_uint8),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264ReferenceInfoFlags',
    },
    'included_in': {
        'VkVideoEncodeH264DpbSlotInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH264ReferenceInfoFlags'},
        'primary_pic_type': {'python_name': ['primary', 'pic', 'type'], 'type': 'StdVideoH264PictureType'},
        'FrameNum': {'python_name': ['frame', 'num']},
        'PicOrderCnt': {'python_name': ['pic', 'order', 'cnt']},
        'long_term_pic_num': {'python_name': ['long', 'term', 'pic', 'num']},
        'long_term_frame_idx': {'python_name': ['long', 'term', 'frame', 'idx']},
        'temporal_id': {'python_name': ['temporal', 'id']},
    }
}
