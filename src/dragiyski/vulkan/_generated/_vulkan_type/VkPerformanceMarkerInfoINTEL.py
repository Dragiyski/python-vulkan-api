import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('marker', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetPerformanceMarkerINTEL',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PERFORMANCE_MARKER_INFO_INTEL', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'marker': {'python_name': ['marker']},
    }
}
