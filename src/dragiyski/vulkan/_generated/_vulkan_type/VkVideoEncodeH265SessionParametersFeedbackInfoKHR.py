import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasStdVPSOverrides', ctypes.c_uint32),
        ('hasStdSPSOverrides', ctypes.c_uint32),
        ('hasStdPPSOverrides', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkVideoEncodeSessionParametersFeedbackInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_FEEDBACK_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'hasStdVPSOverrides': {'python_name': ['has', 'std', 'vpsoverrides']},
        'hasStdSPSOverrides': {'python_name': ['has', 'std', 'spsoverrides']},
        'hasStdPPSOverrides': {'python_name': ['has', 'std', 'ppsoverrides']},
    }
}
