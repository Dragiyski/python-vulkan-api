import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265ReferenceInfoFlags import CType as StdVideoEncodeH265ReferenceInfoFlags

CType._fields_ = [
    ('flags', StdVideoEncodeH265ReferenceInfoFlags),
    ('pic_type', ctypes.c_int),
    ('PicOrderCntVal', ctypes.c_int32),
    ('TemporalId', ctypes.c_uint8),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH265ReferenceInfoFlags',
    },
    'included_in': {
        'VkVideoEncodeH265DpbSlotInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoEncodeH265ReferenceInfoFlags'},
        'pic_type': {'python_name': ['pic', 'type'], 'type': 'StdVideoH265PictureType'},
        'PicOrderCntVal': {'python_name': ['pic', 'order', 'cnt', 'val']},
        'TemporalId': {'python_name': ['temporal', 'id']},
    }
}
