import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH265ReferenceInfoFlags import CType as StdVideoDecodeH265ReferenceInfoFlags

CType._fields_ = [
    ('flags', StdVideoDecodeH265ReferenceInfoFlags),
    ('PicOrderCntVal', ctypes.c_int32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeH265ReferenceInfoFlags',
    },
    'included_in': {
        'VkVideoDecodeH265DpbSlotInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoDecodeH265ReferenceInfoFlags'},
        'PicOrderCntVal': {'python_name': ['pic', 'order', 'cnt', 'val']},
    }
}
