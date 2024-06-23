import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('createFlags', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('type', ctypes.c_int),
        ('deviceAddress', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCreateMicromapEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MICROMAP_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'createFlags': {'python_name': ['create', 'flags'], 'type': 'VkMicromapCreateFlagsEXT'},
        'buffer': {'python_name': ['buffer']},
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
        'type': {'python_name': ['type'], 'type': 'VkMicromapTypeEXT'},
        'deviceAddress': {'python_name': ['device', 'address']},
    }
}
