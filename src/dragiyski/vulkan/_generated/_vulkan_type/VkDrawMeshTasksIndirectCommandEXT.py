import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('groupCountX', ctypes.c_uint32),
        ('groupCountY', ctypes.c_uint32),
        ('groupCountZ', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'groupCountX': {'python_name': ['group', 'count', 'x']},
        'groupCountY': {'python_name': ['group', 'count', 'y']},
        'groupCountZ': {'python_name': ['group', 'count', 'z']},
    }
}
