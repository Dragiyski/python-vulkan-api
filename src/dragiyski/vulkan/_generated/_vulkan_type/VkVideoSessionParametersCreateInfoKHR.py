import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('videoSessionParametersTemplate', ctypes.c_void_p),
        ('videoSession', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoDecodeAV1SessionParametersCreateInfoKHR',
        'VkVideoDecodeH264SessionParametersCreateInfoKHR',
        'VkVideoDecodeH265SessionParametersCreateInfoKHR',
        'VkVideoEncodeH264SessionParametersCreateInfoKHR',
        'VkVideoEncodeH265SessionParametersCreateInfoKHR',
        'VkVideoEncodeQualityLevelInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateVideoSessionParametersKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoSessionParametersCreateFlagsKHR'},
        'videoSessionParametersTemplate': {'python_name': ['video', 'session', 'parameters', 'template']},
        'videoSession': {'python_name': ['video', 'session']},
    }
}
