import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1SequenceHeader import CType as StdVideoAV1SequenceHeader

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdSequenceHeader', ctypes.POINTER(StdVideoAV1SequenceHeader)),
]

descriptor = {
    'extends': {
        'VkVideoSessionParametersCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoAV1SequenceHeader',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_SESSION_PARAMETERS_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pStdSequenceHeader': {'python_name': ['p', 'std', 'sequence', 'header'], 'type': 'StdVideoAV1SequenceHeader'},
    }
}
