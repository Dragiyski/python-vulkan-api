import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pUserData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkInitializePerformanceApiINTEL',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_INITIALIZE_PERFORMANCE_API_INFO_INTEL', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pUserData': {'python_name': ['p', 'user', 'data']},
    }
}
