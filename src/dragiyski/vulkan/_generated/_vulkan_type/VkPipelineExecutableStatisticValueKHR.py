import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('b32', ctypes.c_uint32),
        ('i64', ctypes.c_int64),
        ('u64', ctypes.c_uint64),
        ('f64', ctypes.c_double),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineExecutableStatisticKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'b32': {'python_name': ['b32']},
        'i64': {'python_name': ['i64']},
        'u64': {'python_name': ['u64']},
        'f64': {'python_name': ['f64']},
    }
}
