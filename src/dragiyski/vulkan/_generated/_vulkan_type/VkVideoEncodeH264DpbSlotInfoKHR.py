import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264ReferenceInfo import CType as StdVideoEncodeH264ReferenceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH264ReferenceInfo)),
]

descriptor = {
    'extends': {
        'VkVideoReferenceSlotInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoEncodeH264ReferenceInfo',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_DPB_SLOT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pStdReferenceInfo': {'python_name': ['p', 'std', 'reference', 'info'], 'type': 'StdVideoEncodeH264ReferenceInfo'},
    }
}
