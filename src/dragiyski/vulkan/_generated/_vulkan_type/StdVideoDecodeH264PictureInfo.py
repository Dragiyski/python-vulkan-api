import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH264PictureInfoFlags import CType as StdVideoDecodeH264PictureInfoFlags

CType._fields_ = [
    ('flags', StdVideoDecodeH264PictureInfoFlags),
    ('seq_parameter_set_id', ctypes.c_uint8),
    ('pic_parameter_set_id', ctypes.c_uint8),
    ('reserved1', ctypes.c_uint8),
    ('reserved2', ctypes.c_uint8),
    ('frame_num', ctypes.c_uint16),
    ('idr_pic_id', ctypes.c_uint16),
    ('PicOrderCnt', ctypes.ARRAY(ctypes.c_int32, 2)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeH264PictureInfoFlags',
    },
    'included_in': {
        'VkVideoDecodeH264PictureInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoDecodeH264PictureInfoFlags'},
        'seq_parameter_set_id': {'python_name': ['seq', 'parameter', 'set', 'id']},
        'pic_parameter_set_id': {'python_name': ['pic', 'parameter', 'set', 'id']},
        'reserved1': {'python_name': ['reserved1']},
        'reserved2': {'python_name': ['reserved2']},
        'frame_num': {'python_name': ['frame', 'num']},
        'idr_pic_id': {'python_name': ['idr', 'pic', 'id']},
        'PicOrderCnt': {'python_name': ['pic', 'order', 'cnt']},
    }
}
