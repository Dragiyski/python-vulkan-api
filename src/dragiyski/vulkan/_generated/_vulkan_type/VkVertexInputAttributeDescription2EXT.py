import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('location', ctypes.c_uint32),
        ('binding', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetVertexInputEXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VERTEX_INPUT_ATTRIBUTE_DESCRIPTION_2_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'location': {'python_name': ['location']},
        'binding': {'python_name': ['binding']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'offset': {'python_name': ['offset']},
    }
}
