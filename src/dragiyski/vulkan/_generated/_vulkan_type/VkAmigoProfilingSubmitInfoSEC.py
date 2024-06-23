import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('firstDrawTimestamp', ctypes.c_uint64),
        ('swapBufferTimestamp', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkSubmitInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_AMIGO_PROFILING_SUBMIT_INFO_SEC', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'firstDrawTimestamp': {'python_name': ['first', 'draw', 'timestamp']},
        'swapBufferTimestamp': {'python_name': ['swap', 'buffer', 'timestamp']},
    }
}
