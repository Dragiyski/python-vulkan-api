import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('dataOffset', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint16),
        ('format', ctypes.c_uint16),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'dataOffset': {'python_name': ['data', 'offset']},
        'subdivisionLevel': {'python_name': ['subdivision', 'level']},
        'format': {'python_name': ['format']},
    }
}
