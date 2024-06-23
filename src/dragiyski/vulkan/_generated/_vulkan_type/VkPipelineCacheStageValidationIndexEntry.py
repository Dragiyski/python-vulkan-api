import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('codeSize', ctypes.c_uint64),
        ('codeOffset', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'codeSize': {'python_name': ['code', 'size']},
        'codeOffset': {'python_name': ['code', 'offset']},
    }
}
