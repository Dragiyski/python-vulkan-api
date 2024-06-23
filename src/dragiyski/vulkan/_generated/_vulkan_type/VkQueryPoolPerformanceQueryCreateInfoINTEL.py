import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('performanceCountersSampling', ctypes.c_int),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'performanceCountersSampling': {'python_name': ['performance', 'counters', 'sampling'], 'type': 'VkQueryPoolSamplingModeINTEL'},
    }
}
