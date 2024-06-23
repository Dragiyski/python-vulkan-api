import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH265PictureInfoFlags import CType as StdVideoDecodeH265PictureInfoFlags

CType._fields_ = [
    ('flags', StdVideoDecodeH265PictureInfoFlags),
    ('sps_video_parameter_set_id', ctypes.c_uint8),
    ('pps_seq_parameter_set_id', ctypes.c_uint8),
    ('pps_pic_parameter_set_id', ctypes.c_uint8),
    ('NumDeltaPocsOfRefRpsIdx', ctypes.c_uint8),
    ('PicOrderCntVal', ctypes.c_int32),
    ('NumBitsForSTRefPicSetInSlice', ctypes.c_uint16),
    ('reserved', ctypes.c_uint16),
    ('RefPicSetStCurrBefore', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ('RefPicSetStCurrAfter', ctypes.ARRAY(ctypes.c_uint8, 8)),
    ('RefPicSetLtCurr', ctypes.ARRAY(ctypes.c_uint8, 8)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeH265PictureInfoFlags',
    },
    'included_in': {
        'VkVideoDecodeH265PictureInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoDecodeH265PictureInfoFlags'},
        'sps_video_parameter_set_id': {'python_name': ['sps', 'video', 'parameter', 'set', 'id']},
        'pps_seq_parameter_set_id': {'python_name': ['pps', 'seq', 'parameter', 'set', 'id']},
        'pps_pic_parameter_set_id': {'python_name': ['pps', 'pic', 'parameter', 'set', 'id']},
        'NumDeltaPocsOfRefRpsIdx': {'python_name': ['num', 'delta', 'pocs', 'of', 'ref', 'rps', 'idx']},
        'PicOrderCntVal': {'python_name': ['pic', 'order', 'cnt', 'val']},
        'NumBitsForSTRefPicSetInSlice': {'python_name': ['num', 'bits', 'for', 'stref', 'pic', 'set', 'in', 'slice']},
        'reserved': {'python_name': ['reserved']},
        'RefPicSetStCurrBefore': {'python_name': ['ref', 'pic', 'set', 'st', 'curr', 'before']},
        'RefPicSetStCurrAfter': {'python_name': ['ref', 'pic', 'set', 'st', 'curr', 'after']},
        'RefPicSetLtCurr': {'python_name': ['ref', 'pic', 'set', 'lt', 'curr']},
    }
}
