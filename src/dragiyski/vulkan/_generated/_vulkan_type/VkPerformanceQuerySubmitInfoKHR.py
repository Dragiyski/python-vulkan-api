import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('counterPassIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkSubmitInfo',
        'VkSubmitInfo2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PERFORMANCE_QUERY_SUBMIT_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'counterPassIndex': {'python_name': ['counter', 'pass', 'index']},
    }
}
