import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('divisor', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineVertexInputDivisorStateCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'binding': {'python_name': ['binding']},
        'divisor': {'python_name': ['divisor']},
    }
}
