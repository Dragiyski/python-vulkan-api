import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH265SessionParametersAddInfoKHR import CType as VkVideoEncodeH265SessionParametersAddInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR)),
]

descriptor = {
    'extends': {
        'VkVideoSessionParametersCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoEncodeH265SessionParametersAddInfoKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxStdVPSCount': {'python_name': ['max', 'std', 'vpscount']},
        'maxStdSPSCount': {'python_name': ['max', 'std', 'spscount']},
        'maxStdPPSCount': {'python_name': ['max', 'std', 'ppscount']},
        'pParametersAddInfo': {'python_name': ['p', 'parameters', 'add', 'info'], 'type': 'VkVideoEncodeH265SessionParametersAddInfoKHR'},
    }
}
