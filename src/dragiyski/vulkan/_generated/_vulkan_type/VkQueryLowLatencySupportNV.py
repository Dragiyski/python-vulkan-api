import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pQueriedLowLatencyData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkSemaphoreCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_QUERY_LOW_LATENCY_SUPPORT_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pQueriedLowLatencyData': {'python_name': ['p', 'queried', 'low', 'latency', 'data']},
    }
}
