import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('id', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
        ('pPrivateData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkOpticalFlowSessionCreateInfoNV',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_PRIVATE_DATA_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'id': {'python_name': ['id']},
        'size': {'python_name': ['size']},
        'pPrivateData': {'python_name': ['p', 'private', 'data']},
    }
}
