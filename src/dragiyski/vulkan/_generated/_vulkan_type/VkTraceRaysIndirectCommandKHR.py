import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('width', ctypes.c_uint32),
        ('height', ctypes.c_uint32),
        ('depth', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'width': {'python_name': ['width']},
        'height': {'python_name': ['height']},
        'depth': {'python_name': ['depth']},
    }
}
