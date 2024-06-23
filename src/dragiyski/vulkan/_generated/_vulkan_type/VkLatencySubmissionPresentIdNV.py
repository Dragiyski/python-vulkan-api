import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentID', ctypes.c_uint64),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_LATENCY_SUBMISSION_PRESENT_ID_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'presentID': {'python_name': ['present', 'id']},
    }
}
