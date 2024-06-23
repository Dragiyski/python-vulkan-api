import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265PictureParameterSet import CType as StdVideoH265PictureParameterSet
from .StdVideoH265SequenceParameterSet import CType as StdVideoH265SequenceParameterSet
from .StdVideoH265VideoParameterSet import CType as StdVideoH265VideoParameterSet

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdVPSCount', ctypes.c_uint32),
    ('pStdVPSs', ctypes.POINTER(StdVideoH265VideoParameterSet)),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH265SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH265PictureParameterSet)),
]

descriptor = {
    'extends': {
        'VkVideoSessionParametersUpdateInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'StdVideoH265PictureParameterSet',
        'StdVideoH265SequenceParameterSet',
        'StdVideoH265VideoParameterSet',
    },
    'included_in': {
        'VkVideoEncodeH265SessionParametersCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_ADD_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stdVPSCount': {'python_name': ['std', 'vpscount']},
        'pStdVPSs': {'python_name': ['p', 'std', 'vpss'], 'len': [['stdVPSCount']], 'type': 'StdVideoH265VideoParameterSet'},
        'stdSPSCount': {'python_name': ['std', 'spscount']},
        'pStdSPSs': {'python_name': ['p', 'std', 'spss'], 'len': [['stdSPSCount']], 'type': 'StdVideoH265SequenceParameterSet'},
        'stdPPSCount': {'python_name': ['std', 'ppscount']},
        'pStdPPSs': {'python_name': ['p', 'std', 'ppss'], 'len': [['stdPPSCount']], 'type': 'StdVideoH265PictureParameterSet'},
    }
}
