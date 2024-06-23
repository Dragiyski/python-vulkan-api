import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('optimal', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkFormatProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SUBPASS_RESOLVE_PERFORMANCE_QUERY_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'optimal': {'python_name': ['optimal']},
    }
}
