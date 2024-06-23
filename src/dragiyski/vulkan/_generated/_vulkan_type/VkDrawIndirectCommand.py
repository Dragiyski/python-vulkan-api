import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('vertexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('firstInstance', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'vertexCount': {'python_name': ['vertex', 'count']},
        'instanceCount': {'python_name': ['instance', 'count']},
        'firstVertex': {'python_name': ['first', 'vertex']},
        'firstInstance': {'python_name': ['first', 'instance']},
    }
}
