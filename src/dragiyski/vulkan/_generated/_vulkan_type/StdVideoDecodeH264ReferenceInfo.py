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

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeH264ReferenceInfoFlags',
    },
    'included_in': {
        'VkVideoDecodeH264DpbSlotInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoDecodeH264ReferenceInfoFlags'},
        'FrameNum': {'python_name': ['frame', 'num']},
        'reserved': {'python_name': ['reserved']},
        'PicOrderCnt': {'python_name': ['pic', 'order', 'cnt']},
    }
}
