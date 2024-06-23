import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
        ('divisor', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VERTEX_INPUT_BINDING_DESCRIPTION_2_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'binding': {'python_name': ['binding']},
        'stride': {'python_name': ['stride']},
        'inputRate': {'python_name': ['input', 'rate'], 'type': 'VkVertexInputRate'},
        'divisor': {'python_name': ['divisor']},
    }
}
