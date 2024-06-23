import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoSessionParameters', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoEncodeH264SessionParametersGetInfoKHR',
        'VkVideoEncodeH265SessionParametersGetInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetEncodedVideoSessionParametersKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_GET_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'videoSessionParameters': {'python_name': ['video', 'session', 'parameters']},
    }
}
