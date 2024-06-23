import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('groupIndex', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'groupIndex': {'python_name': ['group', 'index']},
    }
}
