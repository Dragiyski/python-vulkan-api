import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_uint32),
        ('y', ctypes.c_uint32),
        ('z', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'x': {'python_name': ['x']},
        'y': {'python_name': ['y']},
        'z': {'python_name': ['z']},
    }
}
