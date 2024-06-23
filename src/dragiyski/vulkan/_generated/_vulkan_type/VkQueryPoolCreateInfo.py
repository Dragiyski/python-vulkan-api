import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('queryType', ctypes.c_int),
        ('queryCount', ctypes.c_uint32),
        ('pipelineStatistics', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkQueryPoolPerformanceCreateInfoKHR',
        'VkQueryPoolPerformanceQueryCreateInfoINTEL',
        'VkQueryPoolVideoEncodeFeedbackCreateInfoKHR',
        'VkVideoDecodeAV1ProfileInfoKHR',
        'VkVideoDecodeH264ProfileInfoKHR',
        'VkVideoDecodeH265ProfileInfoKHR',
        'VkVideoDecodeUsageInfoKHR',
        'VkVideoEncodeH264ProfileInfoKHR',
        'VkVideoEncodeH265ProfileInfoKHR',
        'VkVideoEncodeUsageInfoKHR',
        'VkVideoProfileInfoKHR',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateQueryPool',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkQueryPoolCreateFlags'},
        'queryType': {'python_name': ['query', 'type'], 'type': 'VkQueryType'},
        'queryCount': {'python_name': ['query', 'count']},
        'pipelineStatistics': {'python_name': ['pipeline', 'statistics'], 'type': 'VkQueryPipelineStatisticFlags'},
    }
}
