import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoDecodeH264SessionParametersAddInfoKHR import CType as VkVideoDecodeH264SessionParametersAddInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoDecodeH264SessionParametersAddInfoKHR)),
]

descriptor = {
    'extends': {
        'VkVideoSessionParametersCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoDecodeH264SessionParametersAddInfoKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_SESSION_PARAMETERS_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxStdSPSCount': {'python_name': ['max', 'std', 'spscount']},
        'maxStdPPSCount': {'python_name': ['max', 'std', 'ppscount']},
        'pParametersAddInfo': {'python_name': ['p', 'parameters', 'add', 'info'], 'type': 'VkVideoDecodeH264SessionParametersAddInfoKHR'},
    }
}
