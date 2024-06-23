import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcAddress', ctypes.c_uint64),
        ('dstAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'srcAddress': {'python_name': ['src', 'address']},
        'dstAddress': {'python_name': ['dst', 'address']},
        'size': {'python_name': ['size']},
    }
}
