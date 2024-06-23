import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('location', ctypes.c_uint32),
        ('binding', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineVertexInputStateCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'location': {'python_name': ['location']},
        'binding': {'python_name': ['binding']},
        'format': {'python_name': ['format'], 'type': 'VkFormat'},
        'offset': {'python_name': ['offset']},
    }
}
