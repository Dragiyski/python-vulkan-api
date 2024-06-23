import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH265ReferenceInfo import CType as StdVideoDecodeH265ReferenceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH265ReferenceInfo)),
]

descriptor = {
    'extends': {
        'VkVideoReferenceSlotInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeH265ReferenceInfo',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_DPB_SLOT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pStdReferenceInfo': {'python_name': ['p', 'std', 'reference', 'info'], 'type': 'StdVideoDecodeH265ReferenceInfo'},
    }
}
