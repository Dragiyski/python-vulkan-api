import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('counterIndexCount', ctypes.c_uint32),
        ('pCounterIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkQueryPoolCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_CREATE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'queueFamilyIndex': {'python_name': ['queue', 'family', 'index']},
        'counterIndexCount': {'python_name': ['counter', 'index', 'count']},
        'pCounterIndices': {'python_name': ['p', 'counter', 'indices'], 'len': [['counterIndexCount']]},
    }
}
