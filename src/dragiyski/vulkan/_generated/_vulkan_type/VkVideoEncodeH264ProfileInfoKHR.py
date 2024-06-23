import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfileIdc', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkQueryPoolCreateInfo',
        'VkVideoProfileInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_PROFILE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stdProfileIdc': {'python_name': ['std', 'profile', 'idc'], 'type': 'StdVideoH264ProfileIdc'},
    }
}
