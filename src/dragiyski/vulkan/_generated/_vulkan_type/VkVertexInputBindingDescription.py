import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
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
        'binding': {'python_name': ['binding']},
        'stride': {'python_name': ['stride']},
        'inputRate': {'python_name': ['input', 'rate'], 'type': 'VkVertexInputRate'},
    }
}
