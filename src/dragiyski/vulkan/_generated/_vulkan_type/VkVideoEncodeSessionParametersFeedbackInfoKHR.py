import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasOverrides', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoEncodeH264SessionParametersFeedbackInfoKHR',
        'VkVideoEncodeH265SessionParametersFeedbackInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetEncodedVideoSessionParametersKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_FEEDBACK_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'hasOverrides': {'python_name': ['has', 'overrides']},
    }
}
