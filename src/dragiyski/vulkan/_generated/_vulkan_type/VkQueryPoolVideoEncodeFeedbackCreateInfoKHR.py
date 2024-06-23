import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('encodeFeedbackFlags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkQueryPoolCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_VIDEO_ENCODE_FEEDBACK_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'encodeFeedbackFlags': {'python_name': ['encode', 'feedback', 'flags'], 'type': 'VkVideoEncodeFeedbackFlagsKHR'},
    }
}
