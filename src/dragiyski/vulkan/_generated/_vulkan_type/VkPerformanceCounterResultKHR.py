import ctypes

class CType(ctypes.Union):
    _fields_ = [
        ('int32', ctypes.c_int32),
        ('int64', ctypes.c_int64),
        ('uint32', ctypes.c_uint32),
        ('uint64', ctypes.c_uint64),
        ('float32', ctypes.c_float),
        ('float64', ctypes.c_double),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'int32': {'python_name': ['int32']},
        'int64': {'python_name': ['int64']},
        'uint32': {'python_name': ['uint32']},
        'uint64': {'python_name': ['uint64']},
        'float32': {'python_name': ['float32']},
        'float64': {'python_name': ['float64']},
    }
}
