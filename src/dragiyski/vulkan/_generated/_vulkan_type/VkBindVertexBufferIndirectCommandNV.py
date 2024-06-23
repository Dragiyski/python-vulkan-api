import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('bufferAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'bufferAddress': {'python_name': ['buffer', 'address']},
        'size': {'python_name': ['size']},
        'stride': {'python_name': ['stride']},
    }
}
