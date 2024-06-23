import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queryPool', ctypes.c_void_p),
        ('firstQuery', ctypes.c_uint32),
        ('queryCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkVideoDecodeInfoKHR',
        'VkVideoEncodeInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_INLINE_QUERY_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'queryPool': {'python_name': ['query', 'pool']},
        'firstQuery': {'python_name': ['first', 'query']},
        'queryCount': {'python_name': ['query', 'count']},
    }
}
