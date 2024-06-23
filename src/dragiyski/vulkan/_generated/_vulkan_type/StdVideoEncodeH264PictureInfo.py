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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264PictureInfoFlags',
        'StdVideoEncodeH264ReferenceListsInfo',
    },
    'included_in': {
        'VkVideoEncodeH264PictureInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH264PictureInfoFlags'},
        'seq_parameter_set_id': {'python_name': ['seq', 'parameter', 'set', 'id']},
        'pic_parameter_set_id': {'python_name': ['pic', 'parameter', 'set', 'id']},
        'idr_pic_id': {'python_name': ['idr', 'pic', 'id']},
        'primary_pic_type': {'python_name': ['primary', 'pic', 'type'], 'type': 'StdVideoH264PictureType'},
        'frame_num': {'python_name': ['frame', 'num']},
        'PicOrderCnt': {'python_name': ['pic', 'order', 'cnt']},
        'temporal_id': {'python_name': ['temporal', 'id']},
        'reserved1': {'python_name': ['reserved1']},
        'pRefLists': {'python_name': ['p', 'ref', 'lists'], 'type': 'StdVideoEncodeH264ReferenceListsInfo'},
    }
}
