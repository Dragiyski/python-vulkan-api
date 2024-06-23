import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('frameToken', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPresentInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PRESENT_FRAME_TOKEN_GGP', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'frameToken': {'python_name': ['frame', 'token']},
    }
}
