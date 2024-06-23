import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('updateSequenceCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoDecodeH264SessionParametersAddInfoKHR',
        'VkVideoDecodeH265SessionParametersAddInfoKHR',
        'VkVideoEncodeH264SessionParametersAddInfoKHR',
        'VkVideoEncodeH265SessionParametersAddInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkUpdateVideoSessionParametersKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_UPDATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'updateSequenceCount': {'python_name': ['update', 'sequence', 'count']},
    }
}
