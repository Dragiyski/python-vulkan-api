import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH264PictureParameterSet import CType as StdVideoH264PictureParameterSet
from .StdVideoH264SequenceParameterSet import CType as StdVideoH264SequenceParameterSet

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH264SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH264PictureParameterSet)),
]

descriptor = {
    'extends': {
        'VkVideoSessionParametersUpdateInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoH264PictureParameterSet',
        'StdVideoH264SequenceParameterSet',
    },
    'included_in': {
        'VkVideoDecodeH264SessionParametersCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_SESSION_PARAMETERS_ADD_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stdSPSCount': {'python_name': ['std', 'spscount']},
        'pStdSPSs': {'python_name': ['p', 'std', 'spss'], 'len': [['stdSPSCount']], 'type': 'StdVideoH264SequenceParameterSet'},
        'stdPPSCount': {'python_name': ['std', 'ppscount']},
        'pStdPPSs': {'python_name': ['p', 'std', 'ppss'], 'len': [['stdPPSCount']], 'type': 'StdVideoH264PictureParameterSet'},
    }
}
