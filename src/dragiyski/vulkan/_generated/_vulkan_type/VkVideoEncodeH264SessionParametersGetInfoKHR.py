import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('writeStdSPS', ctypes.c_uint32),
        ('writeStdPPS', ctypes.c_uint32),
        ('stdSPSId', ctypes.c_uint32),
        ('stdPPSId', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkVideoEncodeSessionParametersGetInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_GET_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'writeStdSPS': {'python_name': ['write', 'std', 'sps']},
        'writeStdPPS': {'python_name': ['write', 'std', 'pps']},
        'stdSPSId': {'python_name': ['std', 'spsid']},
        'stdPPSId': {'python_name': ['std', 'ppsid']},
    }
}
