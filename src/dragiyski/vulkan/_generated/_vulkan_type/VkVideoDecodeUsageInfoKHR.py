import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoUsageHints', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_USAGE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'videoUsageHints': {'python_name': ['video', 'usage', 'hints'], 'type': 'VkVideoDecodeUsageFlagsKHR'},
    }
}
